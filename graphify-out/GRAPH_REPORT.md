# Graph Report - /home/user/ccampbell74  (2026-04-17)

## Corpus Check
- 4 files · ~733 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 44 nodes · 95 edges · 8 communities detected
- Extraction: 51% EXTRACTED · 49% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.67)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]

## God Nodes (most connected - your core abstractions)
1. `BlogService` - 14 edges
2. `PostRepository` - 13 edges
3. `UserRepository` - 12 edges
4. `CommentRepository` - 11 edges
5. `ModerationService` - 11 edges
6. `Post` - 10 edges
7. `User` - 9 edges
8. `Comment` - 8 edges

## Surprising Connections (you probably didn't know these)
- `UserRepository` --uses--> `User`  [INFERRED]
  /home/user/ccampbell74/src/repository.py → /home/user/ccampbell74/src/models.py
- `PostRepository` --uses--> `User`  [INFERRED]
  /home/user/ccampbell74/src/repository.py → /home/user/ccampbell74/src/models.py
- `CommentRepository` --uses--> `User`  [INFERRED]
  /home/user/ccampbell74/src/repository.py → /home/user/ccampbell74/src/models.py
- `BlogService` --uses--> `User`  [INFERRED]
  /home/user/ccampbell74/src/services.py → /home/user/ccampbell74/src/models.py
- `UserRepository` --uses--> `Post`  [INFERRED]
  /home/user/ccampbell74/src/repository.py → /home/user/ccampbell74/src/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (2): User, ModerationService

### Community 1 - "Community 1"
Cohesion: 0.38
Nodes (2): UserRepository, BlogService

### Community 2 - "Community 2"
Cohesion: 0.43
Nodes (2): Comment, CommentRepository

### Community 3 - "Community 3"
Cohesion: 0.4
Nodes (0): 

### Community 4 - "Community 4"
Cohesion: 0.5
Nodes (2): Post, PostRepository

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (0): 

### Community 6 - "Community 6"
Cohesion: 0.5
Nodes (0): 

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (0): 

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlogService` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.216) - this node is a cross-community bridge._
- **Why does `PostRepository` connect `Community 4` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 5`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.212) - this node is a cross-community bridge._
- **Why does `UserRepository` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.193) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `BlogService` (e.g. with `User` and `Post`) actually correct?**
  _`BlogService` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `PostRepository` (e.g. with `User` and `Post`) actually correct?**
  _`PostRepository` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `UserRepository` (e.g. with `User` and `Post`) actually correct?**
  _`UserRepository` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `CommentRepository` (e.g. with `User` and `Post`) actually correct?**
  _`CommentRepository` has 6 INFERRED edges - model-reasoned connections that need verification._