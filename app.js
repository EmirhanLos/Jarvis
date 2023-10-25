const btn = document.querySelector('.talk')
const content = document.querySelector('.content')


function speak(text){
    const text_speak = new SpeechSynthesisUtterance(text);

    text_speak.rate = 1;
    text_speak.volume = 1;
    text_speak.pitch = 1;

    window.speechSynthesis.speak(text_speak);
}

function wishMe(){
    var day = new Date();
    var hour = day.getHours();

    if(hour>=0 && hour<12){
        speak("Günaydın.")
    }

    else if(hour>12 && hour<17){
        speak("İyi günler.")
    }

    else{
        speak("İyi akşamlar.")
    }

}

window.addEventListener('load', ()=>{
    speak("Jarvis başlatılıyor...");
    wishMe();
});

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition =  new SpeechRecognition();

recognition.onresult = (event)=>{
    const currentIndex = event.resultIndex;
    const transcript = event.results[currentIndex][0].transcript;
    content.textContent = transcript;
    takeCommand(transcript.toLowerCase());

}

btn.addEventListener('click', ()=>{
    content.textContent = "Dinliyorum."
    recognition.start();
})

function takeCommand(message){
    if(message.includes('selam') || message.includes('merhaba')){
        speak("Merhaba nasıl yardımcı olabilirim?");
        content.textContent = "Merhaba nasıl yardımcı olabilirim?"
    }
    else if(message.includes("google aç")){
        window.open("https://google.com", "_blank");
        speak("Google açılıyor...")
        content.textContent = "Google açıldı."
    }
    else if(message.includes("youtube aç")){
        window.open("https://youtube.com", "_blank");
        speak("Youtube açılıyor...")
        content.textContent = "Youtube açıldı."
    }
    else if(message.includes("facebook aç")){
        window.open("https://facebook.com", "_blank");
        speak("Facebook açılıyor...")
        content.textContent = "Facebook açıldı."
    }
    
    else if(message.includes('nedir') || message.includes('kim') || message.includes('ne')) {
        window.open(`https://www.google.com/search?q=${message.replace(" ", "+")}`, "_blank");
        const finalText = " " + message + "ile ilgili olarak internette bulduğum şey bu";
	    speak(finalText);
        content.textContent = (finalText)
  
    }

    else if(message.includes('wikipedia')) {
        window.open(`https://en.wikipedia.org/wiki/${message.replace("wikipedia", "")}`, "_blank");
        const finalText2 = " " + message + "ile ilgili olarak wikipedia'da bulduğum şey şudur";
        speak(finalText2);
        content.textContent = (finalText2)
    }

    else if(message.includes('saat')) {
        const time = new Date().toLocaleString(undefined, {hour: "numeric", minute: "numeric"})
        const finalText3 = time;
        speak(finalText3);
        content.textContent = (finalText3)
    }

    else if(message.includes('tarih')) {
        const date = new Date().toLocaleString(undefined, {month: "short", day: "numeric"})
        const finalText4 = date;
        speak(finalText4);
        content.textContent = (finalText4)
    }

    else if(message.includes('hesap makinesini aç')) {
        window.open('Calculator:///')
        const finalText5 = "Hesap makinesi açıldı.";
        speak(finalText5);
        content.textContent = "Hesap makinesi açıldı."
    }

    else if(message.includes('afk')) {
        spanner(document.querySelector('h1'))
    }

    else if(message.includes('evi koru') || message.includes('cihazı koru') || message.includes('cihazları koru')) {
        const defense = "İstediğiniz nesne korunuyor."
        speak(defense);
        content.textContent = (defense)
    }

    else if(message.includes('günaydın')) {
        const morning = "Size de günaydın."
        speak(morning);
        content.textContent = (morning)
    }

    else if(message.includes('iyi geceler')) {
        const bed = "Size de iyi geceler."
        speak(bed);
        content.textContent = (bed)
    }

    else if(message.includes('tünaydın')) {
        const evening = "Size de tünaydın."
        speak(evening);
        content.textContent = (evening)
    }

    else if(message.includes('nasılsın')) {
        const ss1 = "Daima iyiyim."
        speak(ss1);
        content.textContent = (ss1)
    }

    else if(message.includes('jarvis nedir') || message.includes('jarvis kimdir') || message.includes('sen nesin') || message.includes('nesin sen')) {
        const whojarvis = "Ben (Jarvis) Emirhan Karahan tarafından özenle geliştirilen bir yapay zekayım."
        speak(whojarvis);
        content.textContent = (whojarvis)
    }

    else if(message.includes('kendini kapat')) {
        window.close();
    }

    else {
        window.open(`https://www.google.com/search?q=${message.replace(" ", "+")}`, "_blank");
        const finalText6 = "Google da " + message + " için bazı bilgiler buldum.";
        speak(finalText6);
        content.textContent = (finalText6)
    }
}