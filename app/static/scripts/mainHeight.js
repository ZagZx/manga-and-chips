function initMainHeight(){
    const body = document.querySelector('body')
    const header = document.querySelector('header')
    const main = document.querySelector('main')
    const footer = document.querySelector('footer')
    
    main.style.paddingTop = header.offsetHeight + 'px'
    main.style.minHeight = body.offsetHeight + 'px'
    main.style.paddingBottom = footer.offsetHeight + 'px'
}