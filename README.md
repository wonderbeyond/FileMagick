## FileMagick - Tools for files manipulation

```bash
pip install filemagick
```

For example you can keep version string as "0.0.0" in source files
and replace them to the real version at build time.


```bash
filemagick sub __init__.py \
    -p '__version__ = "0.0.0"' -r '__version__ = "0.1.0"'
```

We can use [Python re lookbehind and lookahead assertion](https://www.geeksforgeeks.org/python-regex-lookbehind/)
feature to make out command shorter:

```bash
filemagick sub __init__.py \
    -p '(?<=__version__ = ")0.0.0(?=")' -r '0.1.0'
```

> Note we can use `-i` option to replace the file in place,
> or else just output the replaced content to stdout.

```bash
filemagick sub -i my_service.proto \
    -p 'version: "0.0.0"' -r 'version: "0.1.0"'
```

For more use cases see the test cases in the `tests` directory.
