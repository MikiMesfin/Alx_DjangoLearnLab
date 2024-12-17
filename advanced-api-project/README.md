## Filtering, Searching, and Ordering

### Filtering
- **Endpoint**: `/api/books/`
- **Parameters**: `title`, `author`, `publication_year`
- **Example**: `/api/books/?title=Gatsby&publication_year=1925`

### Searching
- **Endpoint**: `/api/books/`
- **Parameters**: `search`
- **Example**: `/api/books/?search=Gatsby`

### Ordering
- **Endpoint**: `/api/books/`
- **Parameters**: `ordering`
- **Values**: `title`, `-title`, `publication_year`, `-publication_year`
- **Example**: `/api/books/?ordering=-publication_year`
