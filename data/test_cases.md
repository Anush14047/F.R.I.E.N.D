# Manual test cases

| ID | Feature | Preconditions | Steps | Expected result | Execution status |
|---|---|---|---|---|---|
| TC-01 | Chat | Backend running | Send a stress message | Local, empathetic reply appears | Not run |
| TC-02 | Chat validation | Backend running | Submit empty message | Client prevents submission; API returns 422 | Not run |
| TC-03 | Mood creation | Backend running | Pick Calm, add note, save | Entry is persisted and confirmation appears | Not run |
| TC-04 | Mood history | At least one entry | Open Insights | Distribution and recent reflection appear | Not run |
| TC-05 | Mood deletion | At least one entry | Select delete on reflection | Entry disappears from list | Not run |
| TC-06 | Provider failure | External provider unavailable | Use local mode | App continues with local fallback | Not run |
| TC-07 | Safety | Backend running | Send crisis phrase | Direct support, 112 and 14416 resources appear | Not run |
| TC-08 | API errors | Backend running | Delete unknown mood ID | API returns 404 with clear detail | Not run |
| TC-09 | Privacy | App running | Inspect stored data | Only mood/journal data is stored locally; chat is not persisted | Not run |
