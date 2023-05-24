let form = document.querySelector("form");

function verificationChamps() {
    let num = form.numAdresse.value
    let rue = form.rueAdresse.value
    let cp = form.cpAdresse.value
    let ville = form.villeAdresse.value
    let desc = form.description.value


    let message = ""

    if (num === "" || isNaN(num))
        message = message + "Merci de saisir le numéro de l'adresse \n"
    if (rue === "")
        message = message + "Merci de saisir la rue de l'adresse \n"
    if (cp === "" || isNaN(cp))
        message = message + "Merci de saisir le code postale de l'adresse \n"
    if (ville === "")
        message = message + "Merci de saisir la ville de l'adresse \n"
    if (desc === "")
        message = message + "Merci de saisir la descritpion du jardin \n"

    if (message !== "")
        alert(message)

    return (message === "")
}