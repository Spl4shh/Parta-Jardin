function confirmSuppression() {
    Swal.fire({
        title: 'Attention !',
        html: "Etes vous sur de vouloir supprimer votre compte ?",
        icon: 'warning',
        showCancelButton: true,
        cancelButtonText: 'Non',
        confirmButtonText: 'Oui'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: 'Attention !',
                html: "Toute suppression est irréversible, êtes vous certains de vouloir supprimer ?",
                icon: 'warning',
                showCancelButton: true,
                cancelButtonText: 'Annuler',
                confirmButtonText: 'Confirmer'
            }).then((result2) => {
                if (result2.isConfirmed) {
                    return window.location.replace('./user/delete');
                }
            })
        }
    })
    return false
}