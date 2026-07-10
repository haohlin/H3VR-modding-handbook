# Package → Test → Release

~~~mermaid
flowchart LR
  source[Committed source] --> test[Test + verify]
  test --> package[Build package]
  package --> deploy[Deploy]
  deploy --> vr[VR test + logs]
  vr --> publish[Explicit publish approval]
~~~

| Gate | Must be true |
| --- | --- |
| Source | Intentional files only |
| Package | Manifest, README, icon, payload, dependencies correct |
| Deploy | Installed through supported workflow |
| Runtime | Interaction works; logs are clean |
| Publish | User explicitly approves release |

## Primary references

- [Development Flow](../development-flow.md)
- [H3VR Modding Wiki: Thunderstore](https://github.com/H3VR-Modding/wiki/tree/main/src/creating/thunderstore)
- [Mason packaging](https://github.com/H3VR-Modding/Mason/blob/main/docs/src/getting_started/packaging.md)
