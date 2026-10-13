# Louie API for Conversational Analytics

The API runs the same agents and notebooks as the UI, for automation, embedding
and headless use.

## Reference

Your deployment serves its own reference, matching the version you are running:

```
https://<your-louie-host>/api/docs
```

It includes live request testing. Read it there rather than relying on a static
list — endpoints change between versions.

## Authentication

```
Authorization: Bearer <token>
```

## Conversation endpoints

| Endpoint | Use |
|---|---|
| `/chat/` | Start or continue a conversation. Streaming or blocking |
| `/chat_singleshot/` | One request, one answer, no conversation kept |
| `/chat_upload/` | Send a file along with the request |

`/chat_singleshot/` is usually what automation wants: no thread to manage and no
state to clean up.

## Retrieving output

A response refers to the elements it produced rather than inlining them. Fetch
each by its id:

| Endpoint | Returns |
|---|---|
| `/chat/{dthread_id}/binary/{element_id}` | The element itself |
| `/chat/{dthread_id}/binary/{element_id}/info` | Its metadata, without the payload |
| `/chat/{dthread_id}/binary/{element_id}/download` | The same as a file download |

Request `/info` first when you need an element's size or type before deciding
whether to pull it — useful when a response refers to a large dataframe.

Tables can be returned as JSON or Arrow; Arrow is substantially cheaper for
anything large.

## Opening the UI from elsewhere

To hand a user a pre-loaded Louie session from another tool, use a deep link
rather than the API — see [Launch Deep Links](071_Launch_Deep_Links.md).
