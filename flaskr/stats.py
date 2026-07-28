def _count_entries(db):
    cur = db.execute('SELECT COUNT(*) FROM entries')
    return cur.fetchone()[0]


def _latest_entry_title(db):
    cur = db.execute('SELECT title FROM entries ORDER BY id DESC LIMIT 1')
    row = cur.fetchone()
    return row[0] if row else None


def _average_text_length(db):
    cur = db.execute('SELECT text FROM entries')
    rows = cur.fetchall()
    if not rows:
        return 0
    total = sum(len(row['text']) for row in rows)
    return total / len(rows)


def entry_summary(db):
    return {
        'total_entries': _count_entries(db),
        'latest_title': _latest_entry_title(db),
        'average_text_length': _average_text_length(db),
    }
