Requires: 
* Python 3.3
* pyradox.worldmap requires PIL
* pyraodx.yml requires PyYAML

Some scripts are in the root directory. Make sure they actually run before using them as a base, though, I tend to break things after a while. I recommend looking at:
* country_table: Creates a wikitable showing country stats in EU4's 1444 start date.
* military_tech: Shows how to parse a single file.

Module summary:

The most important modules:
pyradox.config: Edit this to point to your game directory.
pyradox.struct: Defines the pyradox.struct.Tree class as well as a pyradox.struct.List class. You'll probably want to read this.
pyradox.txt: Parses Paradox .txt files and puts them into a pyradox.struct.Tree which combines aspects of dicts and ElementTrees. Only the three functions at the top are necessary to know for practical use; the rest is the parser itself.

Other modules:
pyradox.format: Some simple string formatting helpers.
pyradox.image: Some simple image processing helpers.
pyradox.primitive: Some helper functions for managing primitives, as well as a pyradox.primitive.Date and pyradox.primitive.Duration class.
pyradox.worldmap: Used for drawing on world maps. Requires PIL. Not the cleanest code, use at your own risk. Might clean it up later.
pyradox.yml: YML localization.

pyradox.eu4: EU4-specific functionality.
