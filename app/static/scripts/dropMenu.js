function dropMenu(){
    const menu = document.getElementById('menu-content')
    const logo = document.getElementById('user-logo')
    
    if (menu.style.display == 'flex'){
        menu.style.display = 'none'
        logo.style.color = ''
        console.log('virou none')
    }
    else{
        menu.style.display = 'flex'
        logo.style.color = '#ef4444'

        console.log('virou flex')
    }
}