function verif() {
    let dateInput = document.querySelector('#dateRecherche').value

    let dateSaisie = new Date(dateInput)
    let dateDuJour = new Date()
    console.log(dateDuJour, dateSaisie)

    dateAvant = (dateDuJour >= dateSaisie)

    if (dateAvant){
        Swal.fire({
            title: 'Erreur !',
            html: "Merci de saisir une date dans le futur",
            icon: 'warning',
            confirmButtonText: 'OK'
        })
    }

    return !dateAvant
}