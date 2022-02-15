function deleteConfirmation(ticketPK){
    const confirmDelete =  confirm(`Are you sure you want to delete ticket ${ticketPk}?`);
    if (confirmDelete){
        location.href = `delete/${ticketPk}`
    }
}

function setPlaceholderLogin(){
    document.getElementById('id_username').setAttribute('placeholder','Username');
    document.getElementById('id_password').setAttribute('placeholder','Password');
}

function setPlaceholderCommentText(){
    document.getElementById('id_comment').setAttribute('placeholder','Comment');
}