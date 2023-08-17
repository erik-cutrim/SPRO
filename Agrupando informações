[
  {
    "$lookup": {
      "from": "Montadoras",
      "localField": "Montadora",
      "foreignField": "Montadora",
      "as": "MontadoraInfo"
    }
  },
  {
    "$unwind": "$MontadoraInfo"
  },
  {
    "$group": {
      "_id": "$MontadoraInfo.País",
      "Carros": { "$sum": 1 }
    }
  },
  {
    "$project": {
      "_id": 1,
      "Carros": 1
    }
  }
]
