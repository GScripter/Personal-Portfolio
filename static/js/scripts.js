// Menu lateral com transição para as páginas
const nav = document.querySelector(".itens-menu"), 
    navList = nav.querySelectorAll("li"), 
    totalNavList =  navList.length, 
    allSection = document.querySelectorAll(".section"), 
    totalSection = allSection.length;

for(let i=0; i < totalNavList; i++){
    const a = navList[i].querySelector("a"); 
    console.log(a)
    a.addEventListener("click", function(){
        
        //Removendo a classe back-ection
        for (let i=0; i < totalSection; i++){
            allSection[i].classList.remove("back-section");
        }

        for(let j=0; j<totalNavList; j++){

            if(navList[j].querySelector("a").classList.contains("active")){
                // Adicionando a classe back-section
                allSection[j].classList.add("back-section");
            }
            navList[j].querySelector("a").classList.remove("active"); 
        
        }
        this.classList.add("active");
        showSection(this);

        //Para quando selecionado um botão do menu lateral, o mini-menu feche automaticamente
        if(window.innerWidth < 1200){
            lateralSectionBtn();
        }
    })
}

function showSection(element){

    for (let i=0; i < totalSection; i++){
        allSection[i].classList.remove("active");
    }

    const target = element.getAttribute("href").split("#")[1];
          console.log(target)  
          document.querySelector("#" + target).classList.add("active")
}   


// Mini Menu responsivo

const miniMenu = document.querySelector(".mini-menu-button"), 
      lateral = document.querySelector(".lateral");

miniMenu.addEventListener("click", lateralSectionBtn)

function  lateralSectionBtn(){
    lateral.classList.toggle("open");
    miniMenu.classList.toggle("open");
    
    for (let i=0; i < totalSection; i++){
        allSection[i].classList.toggle("open");
    }
}

// Tema Dark
var botao = window.document.getElementById("icone-tema")
botao.addEventListener("click", Tema)
var chk = window.document.getElementById("check")

if(localStorage.tema){
  if(localStorage.tema == "dark"){
    TemaDark()
  }
}

function Tema(){
  if(chk.checked){
    localStorage.setItem("tema", "dark")
    TemaDark()
  }else{
    localStorage.setItem("tema", "light")
    TemaLight()
  }
}

function TemaDark(){
  window.document.getElementsByClassName("bi")[0].classList.remove("bi-toggle-off")
  window.document.getElementsByClassName("bi")[0].classList.add("bi-toggle-on")
  window.document.getElementsByClassName("lateral")[0].style.background = "#343A40"
  // Texto
  var texto = window.document.getElementsByClassName("cor")
  var tot = texto.length - 1
  for(var t =  0; t<=tot; t+=1){
    texto[t].style.color = "#fff"
  }
  // Títulos
  window.document.getElementsByTagName("h1")[0].style.color= "#fff"
  var hsb = window.document.getElementsByTagName("h2")
  var hsc = window.document.getElementsByTagName("h3")
  for(var hb = 0; hb<=3; hb+=1){
    hsb[hb].style.color = "#fff"
  }
  for(var hc = 0; hc<=4; hc+=1){
    hsc[hc].style.color = "#fff"
  }
  // Links
  var link = window.document.getElementsByTagName("a")
  for(var l = 0; l<=5; l+=1){
    link[l].style.color = "#fff"
  }
  // Sessões
  var sessoes = window.document.getElementsByClassName("section")
  for(var s in sessoes){
    sessoes[s].style.background = "#222428"
  }
}

function TemaLight(){
  window.document.getElementsByClassName("bi")[0].classList.remove("bi-toggle-on")
  window.document.getElementsByClassName("bi")[0].classList.add("bi-toggle-off")
  window.document.getElementsByClassName("lateral")[0].style.background = "#fdf9ff"
  // Texto
  var texto = window.document.getElementsByClassName("cor")
  var tot = texto.length - 1
  for(var t =  0; t<=tot; t+=1){
    texto[t].style.color = "#504e70"
  }
  // Títulos
  window.document.getElementsByTagName("h1")[0].style.color= "#504e70"
  var hsb = window.document.getElementsByTagName("h2")
  var hsc = window.document.getElementsByTagName("h3")
  for(var hb = 0; hb<=3; hb+=1){
    hsb[hb].style.color = "#504e70"
  }
  for(var hc = 0; hc<=4; hc+=1){
    hsc[hc].style.color = "#504e70"
  }
  // Links
  var link = window.document.getElementsByTagName("a")
  for(var l = 0; l<=5; l+=1){
    link[l].style.color = "#504e70"
  }
  // Sessões
  var sessoes = window.document.getElementsByClassName("section")
  for(var s in sessoes){
    sessoes[s].style.background = "#f2f2fc"
  }
}

