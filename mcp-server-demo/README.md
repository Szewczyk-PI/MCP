# DNS Check MCP Server

Serwer MCP (Model Context Protocol) zapewniający narzędzia do sprawdzania rekordów DNS oraz czyszczenia tekstu z formatowania Markdown.

## Funkcjonalności

### 1. DNS Check

Sprawdza rekordy DNS dla podanej domeny.

**Parametry:**

- `domain` - nazwa domeny do sprawdzenia (np. `example.com`)
- `record` - typ rekordu DNS (np. `A`, `AAAA`, `MX`, `TXT`, `NS`, `CNAME`)

**Przykład użycia:**

```
domain: google.com
record: A
```

**Zwraca:**
Lista znalezionych rekordów DNS w formacie tekstowym.

### 2. Clean Text

Usuwa znaki formatowania Markdown z podanego tekstu (aktualnie obsługuje gwiazdki `*`).

**Parametry:**

- `tekst` - tekst do wyczyszczenia

**Przykład użycia:**

```
tekst: "To jest **pogrubiony** tekst z *kursywą*"
```

**Zwraca:**

```
To jest pogrubiony tekst z kursywą
```

## Instalacja

### Wymagania

- Python 3.8+
- pip

### Instalacja zależności

```bash
pip install dnspython mcp
pip install dnspython
```

## Uruchomienie

```bash
python main.py
```

## Zależności

- `mcp` - Model Context Protocol server framework
- `dnspython` - biblioteka do zapytań DNS

## Struktura projektu

```
.
├── main.py          # Główny plik serwera
└── README.md          # Ten plik
```

## Przykłady zapytań DNS

- **A Record**: `check_dns("google.com", "A")`
- **MX Record**: `check_dns("gmail.com", "MX")`
- **TXT Record**: `check_dns("example.com", "TXT")`
- **NS Record**: `check_dns("example.com", "NS")`
