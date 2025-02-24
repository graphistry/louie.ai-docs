# Python Sandbox Custom Pip Packages

You can add custom Python packages to the sandbox environment used by L.O.U.I.E.

## Steps

1. **Install the Package to the Sandbox Directory**

   Install the desired package into the sandbox environment:

   ```bash
   docker run --rm -it \
     -v /var/louie/data/data/py_envs/sandbox:/opt/py_envs \
     -e PYTHONPATH=/opt/py_envs \
     -e PIP_TARGET=/opt/py_envs \
     graphistry/louie-sandbox:latest \
     pip install your_package_name
   ```

   - Replace `your_package_name` with the name of the package you wish to install.

2. **Use the Package in Python Cells**

   You can now import and use the package in Python AI and Python cells without restarting Louie.

   Example:

   ```python
   import your_package_name
   # Use the package as needed
   ```

3. **Optional: Restart Services**

   To ensure the AI is aware of the new package's availability, you may restart DJ and Louie:

   ```bash
   cd /var/louie
   ./dc up -d --force-recreate louie
   ```

*This allows for the extension of the sandbox environment with additional Python packages as needed.*