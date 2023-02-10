var nameDict = {
  "ssherman": "Stephanie Sherman",
  "nkhayles": "N. Katherine Hayles",
  "bkonior": "Bogna Konior",
  "bgeoghegan": "Bernard Geoghegan",
  "mseu": "Mindy Seu",
  "rdhaliwal": "Ranjodh Singh Dhaliwal",
  "jparikka": "Jussi Parikka",
  "mbfazi": "M. Beatrice Fazi",
  "jcanales": "Jimena Canales",
  "preed": "Patricia Reed",
  "acavia": "AA Cavia",
  "pfeigelfeld": "Paul Feigelfeld",
  "gmanaugh": "Geoff Manaugh",
  "ajones": "Alexander Jones"
};

for(var key in nameDict) {
  var elems = document.getElementsByClassName(key);
  if (elems == null) {
    continue;
  }
  for (let i = 0; i < elems.length; i++) {
        elems[i].setAttribute("data-text", nameDict[key]);
    }
}
