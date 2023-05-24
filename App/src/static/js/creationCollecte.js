let form = document.querySelector("form");

function verificationChamps() {

    let date = form.datetimeCollecte.value
    let nbEtudiant = form.nombreEtudiant.value
    let actualCard = document.querySelectorAll('.cardProduitDispo')

    let message = ""

    if (date === "")
        message = message + "Merci de saisir la date de la collecte \n"
    if (nbEtudiant === ("" || NaN))
        message = message + "Merci de saisir lle nombre d'étudiants admis à la collècte \n"

    let nomProd;
    let quantiteProd;

    for (let i = 1; i <= actualCard.length; i++) {
        nomProd = document.querySelector('.nomProduit' + i).value
        quantiteProd = document.querySelector('.quantiteProduit' + i).value

        console.log(nomProd)
        if (nomProd === "")
            message = message + "Merci de saisir le nom du produit " + i + " \n"
        if (quantiteProd === "" || quantiteProd == 0)
            message = message + "Merci de saisir la quantité du produit " + i + " \n"
        else if (isNaN(quantiteProd))
            message = message + "Merci de saisir un nombre pour la quantité du produit " + i + " \n"
    }

    if (message !== "")
        alert(message)

    return (message === "")
}


const inputRange = document.querySelector('#inputRange')
const divValueDisplay = document.querySelector("#valueInputRange")
const listeProduitDispo = document.querySelector("#listeProduitDispo")

function updateValue() {
    divValueDisplay.innerHTML = inputRange.value;
}

function editCardQuantity() {
    let nbCard = inputRange.value
    let actualCard = document.querySelectorAll('.cardProduitDispo')
    let nbActualCard = actualCard.length

    let newCard;

    if (nbCard > nbActualCard) {

        let valueInputNomExistant = []
        let valueInputQuantiteExistant = []

        for (let i = 1; i <= nbActualCard; i++) {
            valueInputNomExistant[i] = document.querySelector(".nomProduit"+i).value
            valueInputQuantiteExistant[i] = document.querySelector(".quantiteProduit"+i).value
        }

        for (let i = nbActualCard+1; i <= nbCard; i++) {
            newCard =
                '<div class="cardProduitDispo produit' + i + '"><div><p>Produit ' + i + '</p><input type="text" name="nomProduit' + i + '" class="nomProduit' + i + '"></div>' +
                '<div><p>Quantité estimée (en Kg)</p><input type="number" min=0 value=0 step=0.1 name="quantiteProduit' + i + '" class="quantiteProduit' + i + '"></div></div>'

            listeProduitDispo.innerHTML = listeProduitDispo.innerHTML + newCard
        }

        for (let i = 1; i <= nbActualCard; i++) {
            document.querySelector(".nomProduit"+i).value = valueInputNomExistant[i]
            document.querySelector(".quantiteProduit"+i).value = valueInputQuantiteExistant[i]
        }
    }

    let currentCard;
    if (nbCard < nbActualCard) {
        for (let i = nbActualCard; i > nbCard; i--) {
            currentCard = document.querySelector(".produit" + i)
            currentCard.parentNode.removeChild(currentCard)
        }
    }
}

inputRange.addEventListener('change', updateValue)
inputRange.addEventListener('change', editCardQuantity)
