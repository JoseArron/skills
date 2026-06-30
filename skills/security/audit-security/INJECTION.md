# Injection

The interpreter boundary: untrusted input reaches a query engine, parser, shell, or filesystem and is read as _code or structure_ instead of _data_. The fix is almost always the same shape — keep the data out of the instruction, via parameters, safe APIs, or canonicalization plus an allowlist.

## SQL injection

User input concatenated into a query string is executed as SQL.

```sql
-- VULNERABLE
query = "SELECT * FROM users WHERE id = " + userId

-- SECURE — parameterized; the driver keeps data out of the instruction
query = "SELECT * FROM users WHERE id = ?"
execute(query, [userId])
```

**Primary defense: parameterized queries / prepared statements**, everywhere, including inside ORM raw-query escape hatches. ORMs parameterize by default — the risk is the raw method.

**Injection points that parameters do not cover** — these take _identifiers_, not values, so parameters do not apply; whitelist against a fixed set of allowed columns/directions:

- `ORDER BY` / `GROUP BY` column names and direction
- Table and column names
- `LIMIT` / `OFFSET` (cast to int)
- Dynamic `IN (…)` lists (bind each element)
- `LIKE` patterns (also escape `%` and `_`)

**Defense in depth:** the DB user has least privilege (no DDL, no `xp_cmdshell`), and SQL errors never reach the client.

## XXE (XML External Entity)

An XML parser resolves external entities in user-supplied XML, reading local files or making server-side requests.

Vulnerable wherever XML is parsed — SOAP, XML-RPC, XML uploads, config parsing, RSS/Atom — and in formats that are _secretly_ XML: SVG, SAML assertions, and Office documents (DOCX/XLSX/PPTX are ZIP-wrapped XML).

**Fix: disable DTDs and external entities on the parser.**

```python
# Python — prefer defusedxml, or harden lxml
from lxml import etree
parser = etree.XMLParser(resolve_entities=False, no_network=True)
```

```java
// Java
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

```csharp
// .NET
settings.DtdProcessing = DtdProcessing.Prohibit;
settings.XmlResolver = null;
```

Checklist: DTD processing disabled, external entity + external DTD resolution disabled, XInclude disabled, parser patched, and JSON preferred over XML where the choice exists.

## Path traversal

User input steers a file path, escaping the intended directory with `../` or an absolute path.

```python
# VULNERABLE
file_path = "/uploads/" + user_input        # user_input = "../../etc/passwd"
```

**Best fix: never put user input in a path — use an indirect map.**

```python
files = {"report": "/reports/q1.pdf", "invoice": "/invoices/2024.pdf"}
file_path = files.get(user_input)            # None if not allowlisted
```

**When a path must be derived, canonicalize then confirm containment:**

```python
import os

def safe_join(base_directory, user_path):
    base = os.path.abspath(os.path.realpath(base_directory))
    target = os.path.abspath(os.path.realpath(os.path.join(base, user_path)))
    if os.path.commonpath([base, target]) != base:
        raise ValueError("path escapes base directory")
    return target
```

Reject `..` sequences and absolute-path indicators, and whitelist the filename charset. Resolve symlinks (`realpath`) _before_ the containment check — that is what catches a symlink pointing out of the directory.

## Command & template injection

The same boundary in two more sinks:

- **OS command** — never build a shell string from input. Use an args array with no shell (`execFile`/`subprocess.run([...], shell=False)`), and an allowlist if the command itself is dynamic.
- **Server-side template** — never feed user input as the _template_; pass it as _data_ to a fixed template. User-controlled template strings are remote code execution in most engines.

## Decision shortcut

1. Trace each input to its sink: query, XML parser, file path, shell, template.
2. SQL: is it parameterized? For identifier slots that cannot be, is there a column/direction allowlist?
3. XML: are DTDs and external entities disabled on _this_ parser? Check SVG/DOCX/SAML paths too.
4. Path: indirect map, or canonicalize-then-contain with symlinks resolved first?
5. Shell/template: args array (no shell) and input-as-data (never input-as-template)?
