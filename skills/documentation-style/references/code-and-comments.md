# Code and comments

Use this module when prose refers to code, when a document includes code samples, and when writing documentation comments for an API.

Follow the project's own code style and comment conventions first. Apply the rules below where the project is silent.

## Code in prose

Use code formatting for text that a reader could type, read in a file, or see as output.

- Format these as code: file names, paths, directories, class, method, and function names, attribute and field names and values, element names (without angle brackets), enum names, environment variables, command-line utility names, language keywords, data types, package names, HTTP verbs and header values, port numbers, IP addresses, text the reader enters, and command output.
- Do not format these as code: domain names, product and organization names, and URLs the reader should open in a browser. Link the URL with descriptive text.
- Format a Boolean value as code when you name the value (`true`). Use plain text when you describe the evaluation: "if the check is true".
- Refer to a method without its class unless that would be ambiguous: "call its `get` method", not "call its `animal.get` method".
- Call an HTTP status code a status code, and format the number and name: an HTTP `404 Not Found` status code. Write a range as `2xx`.
- Do not use quotation marks around code unless they are part of the code.
- Do not treat a code element as an English word. Do not make it plural or possessive or use it as a verb. Add a noun and inflect that: "send a `POST` request", not "`POST` the data"; "the `ADDRESS` constant's value", not "`ADDRESS`'s value".
- Do not make a class name plural: "`Intent` objects", not "`Intents`".
- Keep the spelling and capitalization of a code element identical to the source.

## Code samples

- Introduce a sample with a sentence. End it with a colon if the sample follows directly, or with a period if other text comes between.
- Put a sample in a fenced code block and label the language, unless the project's convention differs.
- Follow the indentation and formatting rules of the language's style guide or the project. Most use spaces. Many use two spaces per level.
- Wrap sample lines at 80 characters or fewer when practical.
- Mark omitted code with a comment in the sample's own language, such as `# Several lines are omitted here.` Do not use `...` or an ellipsis character.
- Keep samples minimal, valid, and runnable unless labeled as a fragment.
- Use placeholders in a distinct, consistent form such as `PROJECT_ID`. Tell the reader to replace them.

## API documentation comments

Describe every public class, interface, method, field, constant, and enum. Use the language's own doc-comment format, such as JSDoc, docstrings, or Javadoc.

- Use present tense and specific verbs: "Adds a bird to the list."
- Make the first sentence a short summary of purpose. Tools show it alone in indexes. Do not end it early with `e.g.`; use "for example".
- Do not repeat the name of the item in the first sentence. Do not write "This class…".
- Put detail after the first sentence: how to use it, prerequisites, side effects, exceptions, related APIs.

### Classes

- State the purpose in a way the name and signature do not already show.
- Then explain how to create or call it, key features, and pitfalls.

### Methods

- Start with a verb for the action. Use "Checks whether…" for a Boolean getter and "Gets the…" for other getters. Use "Sets", "Updates", "Deletes", "Registers", and "Creates a…" as fits.
- Document required permissions or dependencies and what happens when they are missing.
- Document exceptions.

### Parameters and return values

- Capitalize the first word and end with a period.
- Start a non-Boolean parameter description with "The" or "A".
- For a Boolean that triggers behavior, state both outcomes: "If true, validates the certificate. If false, trusts it without validating."
- For a Boolean that reports state, write "True if…; false otherwise."
- For defaults, describe the behavior for each value, then write "Default:" and the value.
- Keep return descriptions brief. Start with "The…", or "True if…; false otherwise." for a Boolean. Put detail in the class or method description.
- Start an exception description with "If…" when the tool adds "Throws". Otherwise start with "Thrown when…".

### Fields and constants

- Keep descriptions as short as possible. Reference the methods that use them.

### Deprecations

- Say what to use instead and, where versions are tracked, when it was deprecated.
- Put the replacement in the first sentence: "Deprecated. Use `newMethod` instead."

## Inline code comments

These are local standards, not Google guidance.

- Explain why the code does something, not what it does.
- Delete comments that restate the code.
- Update or remove a comment when the code it describes changes.

## Provenance

The code-in-prose, code sample, and API comment rules come from the Google developer documentation style guide pages "Code in text", "Code samples", and "API reference comments". Two points differ from that guide: fenced blocks replace four-space indentation in Markdown, and the inline comment rules are local.
