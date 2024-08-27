const verses = [
  {
    verse: "phillipians 1:4-5",
    cont: "In all my prayers for all of you, I always pray with joy because of your patnership in the gospel from the first day until now"
  },
  {
    verse: "Jeremiah 1:5",
    cont: "Before I formed you in the womb I knew you, before you were born I set you apart"
  },
  {
    verse: "ROMANS 8: 38-39",
    cont: "Neither death, nor life, nor angels, nor rulers, nor things present, nor things to come, nor powers, nor height, nor depth, nor anything else in all creation, will be able to separate us from the love of God in Christ Jesus our Lord"
  },
  {
    verse: "psalms 127:1",
    cont: "If the Lord does not build the house, the work of the builders is useless; if the lord does not protect the city,it is uselless foor the sentries to stand guard"
  },
  {
    verse: "john 4:13-14",
    cont: "jesus answered, 'All those who driink this water will be thirsty again,but whoever drinks the water that I will give him will never be thirsty"
  },
  {
    verse: "Deutoronomy 11:13-21",
    cont: "so then obey the commands that I have given you today; love the lord your God and serve him with all your heart ,v14, If you do, he will send rain on your land when it is needed .."
  },
  {
    verse: "Hebrews 13:9",
    cont: "Do not let all kinds of teachings lead you away from the right way. It is good to recieve inner strength from God's grace,and not obeying rules about foods;those who obey these rules have not been helped by them "
  },
  {
    verse: "John 1:1o-18",
    cont: "The word was in the world,and though God made the world through him,yet the world the world did not recognize him ,v11  he came to his own country ,but his own people did not receive , v12 Some ,however, did recieve him and believed in him; so he gave them the right to be God's children"
  },
  {
    verse: "matthew 16:13-21",
    cont: "Jesus went to the territory of near the toen of caesarea Philippi, where he asked his disciples, 'who do people say the son of man is?' ' some say john the baptist' they answered . 'others say Elijah, while others say jeremiah' 'what abouth you who do you say i am' he asked them simon peter answered, 'you are the messiah the son of the living God "
    
  },
  {
    verse: "matthew 25:31-40",
    cont: "whoever is kind to the poor lends to the lord, and he will reward them for what they have done(proverbs 19:17)"
  },
  {
    verse: "John 5:1-8",
    cont: "When jesus saw him lying there ... he asked him,'Do you want to get well?'(v.6)"
  },
  {
    verse: "John 3:22-35",
    cont: "he must become greater; I must become less"
  },
  {
    verse: "Genesis 29:31-35",
    cont: "She concieved again, and when she gave birth to a son she said, 'This time I will praise the lord"
  },
]

let verse =  document.querySelector('.verseOfInput').value
let counter = localStorage.getItem('day')
let count = parseInt(localStorage.getItem('count'))
let length = count > verses.length -1


if (!counter){
  localStorage.setItem('day', verse)
  counter = localStorage.getItem('day')
}

if(!count){
  count = '0'
  localStorage.setItem('count',count)
}

if(document.querySelector('.verse-of')){

  verse =  document.querySelector('.verseOfInput').value
  let verseHolder = document.querySelector('.verse-of')
  let verseHome = verseHolder.querySelector('.background-words')
  
  if(verse !== counter){
    count = parseInt(localStorage.getItem('count'))
    length ? count = 0 :count ++ ;
    verseHome.innerHTML = `
    <h2>verse of the day</h2>
    <br>
    <p>
      "${ verses[count].cont}"
      <br>
      <span class="quoted-word">
      ${ verses[count].verse}
      </span>
    </p>
    `
    localStorage.setItem('count',count)
  }else{
    count = parseInt(localStorage.getItem('count'))
    verseHome.innerHTML = `
    <h2>verse of the day</h2>
    <br>
    <p>
      "${ verses[count].cont}"
      <br>
      <span class="quoted-word">
      ${ verses[count].verse}
      </span>
    </p>
    `
  }
}

if(document.querySelector('.final')){
  verse =  document.querySelector('.verseOfInput').value
  let archverse = document.querySelector('.final')
  let arch = archverse.querySelector('.more-p')
  
  if(verse !== counter){
    localStorage.setItem('day', verse)
    count = parseInt(localStorage.getItem('count'))
    length ? count = 0 :count ++ ;
    arch.innerHTML= `
      <p>
          "${ verses[count].cont}"
        </p>
        <span>
        ${ verses[count].verse}
        </span>
      `
    localStorage.setItem('count',count)
  }else{
    count = parseInt(localStorage.getItem('count'))
    arch.innerHTML= `
      <p>
          "${ verses[count].cont}"
        </p>
        <span>
        ${ verses[count].verse}
        </span>
      `
  }
}
