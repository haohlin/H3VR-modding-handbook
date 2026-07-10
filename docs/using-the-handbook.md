# How to Use the Handbook

## Use this route when

You have opened the handbook and need to decide whether to read online, clone
the references, update a submodule, or begin real mod work.

## Three ways to use the repository

### 1. Browse it on GitHub

Use this when you are learning a route or need a link quickly.

1. Open [Start Here](start-here.md).
2. Choose the guide that matches your deliverable.
3. Open the route's Primary references section.
4. Use the [navigation index](navigation/index.md) when you know the topic but
   not the source project.
5. Use the [mind map](navigation/mind-map.md) when you want the larger
   relationship between tools and workflows.

### 2. Clone it as a local study library

Use this when you want to search original Markdown, inspect project layout, or
compare implementation patterns.

~~~bash
git clone --recurse-submodules https://github.com/h3vr-modding/H3VR-modding-handbook.git
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
~~~

A full clone contains pinned upstream projects under references/. They are
reference material, not a shared development checkout.

To initialize one missing reference instead of all references:

~~~bash
git submodule update --init references/H3VR-Modding/Mason
~~~

### 3. Start an actual mod change

Use this when the handbook has directed you to the correct route.

1. Read the route guide and its primary references.
2. Open the authoritative Windows workspace named by
   [Development Flow](development-flow.md).
3. Make the change in that workspace, not inside references/.
4. Build/package/deploy using the established project workflow.
5. Run an in-game test and inspect runtime logs.
6. Commit the real source repository separately from handbook documentation.

## Keep the library trustworthy

- A submodule is a pinned upstream commit, not a fork to edit here.
- Use a user-provided raw note only as context; re-check version-sensitive
  instructions against the primary source.
- Source cards are links, not copied third-party documentation.
- Run the verifier before committing handbook changes:

~~~bash
python3 -m unittest tests/test_reference_manifest.py -v
python3 scripts/verify_handbook.py
~~~

## Primary references

- [Start Here](start-here.md)
- [Development Flow](development-flow.md)
- [Navigation index](navigation/index.md)
- [Source policy](../SOURCES.md)
- [Contributing](../CONTRIBUTING.md)

