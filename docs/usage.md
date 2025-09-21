# Usage

The CLI uses a resource-first syntax. Examples:

- List serial ports:

```bash
iomx serial ls
```

- Run the Textual TUI (requires `textual`):

```bash
iomx tui
```

- Show version:

```bash
iomx version
```

The code is structured so each resource maps to a Python module under `iomx.commands`.
For example, the `serial` resource is implemented by `iomx.commands.lsserial` (for now). To add more functionality, add subcommands under the `serial` parser and wire them to `iomx.commands.serial` or `iomx.commands.lsserial` functions.
