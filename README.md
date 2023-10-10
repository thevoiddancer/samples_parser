# lark_samples
Lark code to parse the samples for the samples_revived repo.

In addition, the repo holds a short tutorial on lark use, applied on this
particular problem

## Samples syntax
Syntax is quite complex, with basic structure clear, but with multiple additions.

### Basic syntax
Basic syntax example follows:
```
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
```


### Additional syntax
Additionally, depending on the sample type, expanded syntax is possible:
```
  "..."            Basic sample

  "'...'           
   '...'"          Sample with conversation

  "... <???> ..."  Sample with unclear part

  "... [...] ..."  Sample with a sound effect

  [...]            Pure sound effect

  "[...]"          Pure sound effect (but rewared a point in the old site)

  "..." @ M:SS     Timestamp of the sample
```

Clearly, additional syntax complicates the parsing significantly, 
so will be ignored for the time being.

## Roadmap:

1. Parse samples:
  - create parser
  - create transformer
  - parse and transforme to a pickle
2. Store samples:
  - create database model
  - store in database (sqlite)
