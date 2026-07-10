# Package, Test, and Release

## Use this route when

You have a candidate mod or content package that needs repeatable verification
before a Thunderstore release.

## Release checklist

1. Commit only intentional source, metadata, and documentation changes.
2. Run the repository tests and type-specific validation in the authoritative
   Windows environment.
3. Build and package with the established wrapper/toolchain. Inspect the package
   manifest, README, icon, dependency metadata, and payload layout.
4. Deploy only the successfully packaged artifact through the supported deploy
   flow.
5. Ask a VR tester to exercise the actual interaction. Review BepInEx and Unity
   errors after the test.
6. Publish only with explicit user authorization and an approved VR result where
   the package workflow requires it.
7. Record the final package version, commit, checksum/receipt, and known
   dependencies in the release notes.

## Primary references

- [Development flow](../development-flow.md)
- [H3VR Modding Wiki Thunderstore source](../../references/H3VR-Modding/wiki/src/creating/thunderstore)
- [Mason packaging source](../../references/H3VR-Modding/Mason/docs/src/getting_started/packaging.md)

