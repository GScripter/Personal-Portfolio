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


// Dark Theme
function DarkTheme(){
  localStorage.theme = 'dark'
  window.document.body.classList.add('dark')
  window.document.getElementsByClassName('bi-toggle-off')[0].classList.add('bi-toggle-on')
  window.document.getElementsByClassName('bi-toggle-off')[0].classList.remove('bi-toggle-off')
}


// Light Theme
function DefaultTheme(){
  localStorage.theme = 'default'
  window.document.body.classList.remove('dark')
  window.document.getElementsByClassName('bi-toggle-on')[0].classList.add('bi-toggle-off')
  window.document.getElementsByClassName('bi-toggle-on')[0].classList.remove('bi-toggle-on')
}


function theme(){
  var ThemeChk = window.document.getElementById('check')
  if(ThemeChk.checked){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}


if(localStorage.theme){
  if(localStorage.theme == "dark"){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}

