# mock-fs
Simple proof-of-concept mock file system example written in python 3.

## Usage
The application can be imported as a python package `mockfs`.

#### Importing
If launching python from the project root folder, this can be accomplished through:
```
import mockfs
```
The primary file system object is the `MockFileSystem` class.
#### Example
```
from mockfs import MockFileSystem
fs = MockFileSystem()

fs.Create('drive', 'C', None)
fs.Create('folder', 'f', 'C')
fs.Create('text', 'text.txt', 'C\\f')
fs.WriteToFile('C\\f\\text.txt', 'Hello World')
fs.Delete('C\\f\\text.txt')
```

> Additional usage examples can be seen in the `test` folder

### Running Tests
To run all unit tests, enter the following command from the `mock-fs` project directory:
> python3 -m unittest

## Documentation Notes
Several assumptions needed to be made when designing the system. 
To avoid confusion several relevant decisions have been listed below:
- Pythonic naming conventions were mostly followed,
however property and function names specifically mentioned in the specifications
were preserved whereever possible
- Entity properties are primarily implemented as python properties.
  - Currently this doesn't make a large difference, but it does allow internal
representations to differ from the exposed API without substantial changes.
It also limits direct access to the entity's internals.

### Additional Notes
- uses built-in `FileNotFoundError` for _Path not found_ exception
- uses built-in `FileExistsError` for _Path already exists_ exception
- the WriteToFile method is expected overwrite any existing content in the target text file
- the Delete method will also delete all child elements

### Specifications
The complete specifications can be found on the wiki under [Assignment Specifications](https://github.com/lwthatcher/mock-fs/wiki/Assignment-Specifications)
