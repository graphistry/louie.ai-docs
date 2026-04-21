# Graphistry Iframe Blocked in Louie

Diagnose and fix "This content is blocked. Contact the site owner to fix the issue." (or blank/looping iframe) when a Louie thread renders a Graphistry graph.

## When this applies

Louie and Graphistry are deployed on **different origins** (different hostnames, or different subdomains with different cookie scopes), even if they sit behind the same proxy or on the same box. Cross-origin embedding depends on **cookie policy and CSP alignment** — not on `X-Frame-Options` alone.

If Louie and Graphistry are served from the exact same origin, this runbook does not apply.

## Three-way host alignment

For cross-origin iframes to authenticate and render, **three hosts must be the same value**:

1. Louie's `OA2_HOST` (the Graphistry OAuth2 host Louie redirects users to)
2. The Graphistry browser-facing host that serves the iframe
3. The host listed in Louie Caddy's CSP `frame-src` **and** `child-src`

A mismatch between any pair causes the iframe to be blocked by the browser or to loop on auth.

## Required settings

### Graphistry side (cross-origin cookies)

In the Graphistry server's `custom.env`:

```bash
COOKIE_SECURE=true
COOKIE_SAMESITE=None
```

These are the defaults. Confirm they are not overridden by a site-specific `custom.env`.

Symptom of a wrong value: Graphistry session cookies come back as `SameSite=Lax`, so the browser drops them from the Louie-embedded iframe and auth loops indefinitely.

Verify in the browser DevTools → Application → Cookies on the Graphistry host:

- Working: `SameSite=None; Secure`
- Failing: `SameSite=Lax`

### Louie side (CSP and OA2_HOST)

In Louie's Caddy config, the Graphistry host must appear in **both** `frame-src` and `child-src`:

```
Content-Security-Policy "... frame-src 'self' https://your.graphistry-server.xyz; child-src 'self' https://your.graphistry-server.xyz; ..."
```

In Louie's `custom.env`:

```bash
OA2_HOST='https://your.graphistry-server.xyz'
```

The hostname in `OA2_HOST` must exactly match the CSP entries above and the host actually serving Graphistry to the browser.

## Diagnosis checklist

Run these in order. Stop at the first mismatch.

1. **Confirm origins differ.** If Louie and Graphistry share a single origin, this page is not your problem.
2. **Inspect the browser console** on the failing page. "Refused to frame … because it violates CSP `frame-src`/`child-src`" points to the Louie CSP. A cookie warning about `SameSite` points to Graphistry cookie flags.
3. **Check Graphistry cookies** on the Graphistry host (DevTools → Application → Cookies). Require `SameSite=None; Secure` on session cookies.
4. **Check Louie's CSP response header** (DevTools → Network → the Louie HTML response). Confirm `frame-src` and `child-src` both include the Graphistry host literally.
5. **Compare hostnames.** `OA2_HOST` value in Louie's `custom.env` should be byte-identical to the Graphistry host in CSP and to the host the browser actually loads Graphistry from (follow redirects).
6. **Confirm Graphistry `custom.env`** does not override `COOKIE_SECURE` or `COOKIE_SAMESITE`.

## Fix

Apply the missing piece from the checklist above, then restart the affected service:

Graphistry:

```bash
cd /var/graphistry
./dc up -d --force-recreate caddy
```

Louie:

```bash
cd /var/louie
./dc up -d --force-recreate caddy louie api
```

Reload the Louie page in a fresh browser context (clear the Graphistry cookies first if you changed cookie flags).

## Related docs

- Louie authentication configuration: [Authentication Registration & TLS](011_Authentication_Registration.md) — covers `OA2_HOST`, `OA2_REDIRECT_URL_BASE`, and the Caddy TLS pattern.
- Graphistry server administration: [graphistry/graphistry-cli](https://github.com/graphistry/graphistry-cli) — server profiles, cookie flags, and test steps for cross-origin vs single-origin embedding.
