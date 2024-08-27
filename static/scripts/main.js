const observed = document.querySelector('.intro')


const observer = new IntersectionObserver(
  entry=>{
    const header = document.body.querySelector('header')
    header.classList.toggle("active-header", entry.isIntersecting)
  },{
    threshold: 0.5,
  }
)

observer.observe(observed)



document.querySelector('.hashbar-container').onclick = () =>{
  document.querySelector('.context-menu').dataset.active = 'true'
  document.body.dataset.menu = 'true'
}

document.querySelector('.x').onclick = () =>{
  document.querySelector('.context-menu').removeAttribute('data-active')
  document.body.removeAttribute('data-menu')
}

document.querySelectorAll('.added-context').forEach( context =>{
  context.addEventListener('click', ()=>{
    context.closest('.context-items').querySelector('.extra').dataset.active !== 'true'?
    context.closest('.context-items').querySelector('.extra').dataset.active = 'true':context.closest('.context-items').querySelector('.extra').dataset.active = 'false'
  })
})

 const clickable = document.querySelectorAll('.clickable')
 clickable.forEach( clickable =>{
  clickable.addEventListener('click', ()=>{
    document.querySelector('.context-menu').removeAttribute('data-active')
    document.body.removeAttribute('data-menu')
  })
 })

setInterval( function animate(){
  slides = [...document.querySelector('.carousel').querySelectorAll('.intro')]
  activeSlide = document.querySelector('.carousel').querySelector('[data-active]')
  let offset = slides.indexOf(activeSlide)
  offset += 1
  if(offset >= slides.length) offset = 0
  nextSlide = slides[offset]
  nextSlide.dataset.active = 'true'
  delete activeSlide.dataset.active
},10000)

buttons = document.querySelectorAll('[data-carousel]')
buttons.forEach(button => {
  button.addEventListener('click', ()=>{
    slides = [...button.closest('.carousel').querySelectorAll('.intro')]
    activeSlide = button.closest('.carousel').querySelector('[data-active]')       
    let offset = slides.indexOf(activeSlide)
    button.dataset.carousel === 'next' ?offset += 1 : offset -=1
    if(offset >= slides.length) offset = 0
    if (offset < 0) offset = slides.length - 1
    nextSlide = slides[offset]
    nextSlide.dataset.active = 'true'
    delete activeSlide.dataset.active
  })
})