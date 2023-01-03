import streamlit as st
import streamlit.components.v1 as com
st.title("Welcome !")
com.html(
    """
<html>
  <head>
    <meta charset="utf-8" />
    <title>Speech to text</title>
    # <style>
    #   body {
    #     font-family: arial;
    #     font-size: 16px;
    #     margin: 0;
    #     background: linear-gradient(to right bottom, #d13cff, #031f6a);
    #     color: #000;

    #     display: flex;
    #     align-items: center;
    #     justify-content: center;
    #     min-height: 100vh;
    #   }
    #   .voice_to_text {
    #     width: 600px;
    #     text-align: center;
    #   }
    #   .container {
    #     text-align: center;
    #     margin-top: 100px;
    #   }
    #   textarea {
    #     width: 500px;
    #     height: 250px;
    #     resize: none;
    #     font-size: 16px;
    #     padding: 10px 15px;
    #   }
    #   h1 {
    #     color: #fff;
    #     font-size: 50px;
    #   }
    #   button {
    #     margin-top: 10px;
    #   }
    #   #confd {
    #     margin-top: 10px;
    #   }
    #   #countryLang {
    #     display: none;
    #   }
    # </style>
    <style>
      body {
        font-family: arial;
        font-size: 16px;
        margin: 0;
        background: linear-gradient(to right bottom, #d13cff, #031f6a);
        color: #000;

        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
      }
      .voice_to_text {
        width: 600px;
        text-align: center;
      }
      .container {
        
        text-align: center;
        # margin-top: 10%;
      }
      textarea {
        width: 100%;
        height: 5%;
        resize: none;
        font-size: ;
        padding: 10px 15px;
      }
      h1 {
        color: #fff;
        font-size: 10px;
      }
      button {
        margin-top: 10px;
      }
      #confd {
        margin-top: 10px;
      }
      #countryLang {
        display: none;
      }
      .heading{
        font-size:100%;
      }
    </style>
  </head>

  <body>
    <div class="container">
	  <h1 class = "heading">Real Time Voice To Text Generator</h1>
      <textarea id="output"></textarea><br />
      <button id="start">Start</button>
      <button id="stop">Stop</button>
      <button id="cancel">Cancel</button>
      <select id="country"></select>
      <select id="countryLang"></select>
      <div id="confd">----</div>
    </div>
    <script>
      var output = document.getElementById("output");
      var start = document.getElementById("start");
      var stop = document.getElementById("stop");
      var cancel = document.getElementById("cancel");
      var country = document.getElementById("country");
      var countryLang = document.getElementById("countryLang");
      var confd = document.getElementById("confd");

      // now lets use web speech api
      var speechRecognition = speechRecognition || webkitSpeechRecognition;
      var recognizer = new speechRecognition();
      // new get languages from array supported by api
      // first copy array from a website

      var langList = [
        ["Afrikaans", ["af-ZA"]],
        ["አማርኛ", ["am-ET"]],
        ["Azərbaycanca", ["az-AZ"]],
        ["বাংলা", ["bn-BD", "বাংলাদেশ"], ["bn-IN", "ভারত"]],
        ["Bahasa Indonesia", ["id-ID"]],
        ["Bahasa Melayu", ["ms-MY"]],
        ["Català", ["ca-ES"]],
        ["Čeština", ["cs-CZ"]],
        ["Dansk", ["da-DK"]],
        ["Deutsch", ["de-DE"]],
        [
          "English",
          ["en-AU", "Australia"],
          ["en-CA", "Canada"],
          ["en-IN", "India"],
          ["en-KE", "Kenya"],
          ["en-TZ", "Tanzania"],
          ["en-GH", "Ghana"],
          ["en-NZ", "New Zealand"],
          ["en-NG", "Nigeria"],
          ["en-ZA", "South Africa"],
          ["en-PH", "Philippines"],
          ["en-GB", "United Kingdom"],
          ["en-US", "United States"],
        ],
        [
          "Español",
          ["es-AR", "Argentina"],
          ["es-BO", "Bolivia"],
          ["es-CL", "Chile"],
          ["es-CO", "Colombia"],
          ["es-CR", "Costa Rica"],
          ["es-EC", "Ecuador"],
          ["es-SV", "El Salvador"],
          ["es-ES", "España"],
          ["es-US", "Estados Unidos"],
          ["es-GT", "Guatemala"],
          ["es-HN", "Honduras"],
          ["es-MX", "México"],
          ["es-NI", "Nicaragua"],
          ["es-PA", "Panamá"],
          ["es-PY", "Paraguay"],
          ["es-PE", "Perú"],
          ["es-PR", "Puerto Rico"],
          ["es-DO", "República Dominicana"],
          ["es-UY", "Uruguay"],
          ["es-VE", "Venezuela"],
        ],
        ["Euskara", ["eu-ES"]],
        ["Filipino", ["fil-PH"]],
        ["Français", ["fr-FR"]],
        ["Basa Jawa", ["jv-ID"]],
        ["Galego", ["gl-ES"]],
        ["ગુજરાતી", ["gu-IN"]],
        ["Hrvatski", ["hr-HR"]],
        ["IsiZulu", ["zu-ZA"]],
        ["Íslenska", ["is-IS"]],
        ["Italiano", ["it-IT", "Italia"], ["it-CH", "Svizzera"]],
        ["ಕನ್ನಡ", ["kn-IN"]],
        ["ភាសាខ្មែរ", ["km-KH"]],
        ["Latviešu", ["lv-LV"]],
        ["Lietuvių", ["lt-LT"]],
        ["മലയാളം", ["ml-IN"]],
        ["मराठी", ["mr-IN"]],
        ["Magyar", ["hu-HU"]],
        ["ລາວ", ["lo-LA"]],
        ["Nederlands", ["nl-NL"]],
        ["नेपाली भाषा", ["ne-NP"]],
        ["Norsk bokmål", ["nb-NO"]],
        ["Polski", ["pl-PL"]],
        ["Português", ["pt-BR", "Brasil"], ["pt-PT", "Portugal"]],
        ["Română", ["ro-RO"]],
        ["සිංහල", ["si-LK"]],
        ["Slovenščina", ["sl-SI"]],
        ["Basa Sunda", ["su-ID"]],
        ["Slovenčina", ["sk-SK"]],
        ["Suomi", ["fi-FI"]],
        ["Svenska", ["sv-SE"]],
        ["Kiswahili", ["sw-TZ", "Tanzania"], ["sw-KE", "Kenya"]],
        ["ქართული", ["ka-GE"]],
        ["Հայերեն", ["hy-AM"]],
        [
          "தமிழ்",
          ["ta-IN", "இந்தியா"],
          ["ta-SG", "சிங்கப்பூர்"],
          ["ta-LK", "இலங்கை"],
          ["ta-MY", "மலேசியா"],
        ],
        ["తెలుగు", ["te-IN"]],
        ["Tiếng Việt", ["vi-VN"]],
        ["Türkçe", ["tr-TR"]],
        ["اُردُو", ["ur-PK", "پاکستان"], ["ur-IN", "بھارت"]],
        ["Ελληνικά", ["el-GR"]],
        ["български", ["bg-BG"]],
        ["Pусский", ["ru-RU"]],
        ["Српски", ["sr-RS"]],
        ["Українська", ["uk-UA"]],
        ["한국어", ["ko-KR"]],
        [
          "中文",
          ["cmn-Hans-CN", "普通话 (中国大陆)"],
          ["cmn-Hans-HK", "普通话 (香港)"],
          ["cmn-Hant-TW", "中文 (台灣)"],
          ["yue-Hant-HK", "粵語 (香港)"],
        ],
        ["日本語", ["ja-JP"]],
        ["हिन्दी", ["hi-IN"]],
        ["ภาษาไทย", ["th-TH"]],
      ];

      // first select a default language on page load
      recognizer.lang = "en-US";
      // now create a list of language to select on page
      for (var i = 0; i < langList.length; i++) {
        // add it in the select tag
        var countryList =
          countryList +
          '<option value="' +
          i +
          '">' +
          langList[i][0] +
          "</option>";
      }
      country.innerHTML = countryList;
      // some languages are used in more that one country Now specify languages for country
      country.onchange = function () {
        var countryVal = country.value;
        // we have to give the array variable to get data "langList"
        var selectCount = langList[countryVal];
        if (selectCount.length <= 2) {
          var countryLangList =
            countryLangList +
            '<option value="' +
            selectCount[1][0] +
            '">' +
            selectCount[0] +
            "</option>";
        } else {
          for (var j = 1; j < selectCount.length; j++) {
            var countryLangList =
              countryLangList +
              '<option value="' +
              selectCount[j][0] +
              '">' +
              selectCount[j][1] +
              "</option>";
          }
        }
        countryLang.innerHTML = countryLangList;
        countryLang.style.display = "inline-block";
        recognizer.lang = countryLang.value;
      };
      // first set the value for lang
      countryLang.onchange = function () {
        // it will get the value and assign to the "recognizer.lang" on selecting
        recognizer.lang = countryLang.value;
      };
      // now set controls
      start.onclick = function () {
        recognizer.start();
      };
      stop.onclick = function () {
        recognizer.stop();
      };
      cancel.onclick = function () {
        recognizer.abort();
        confd.innerHTML = "The Session is been cancelled...";
      };
      // when the recognizing start
      recognizer.onstart = function () {
        confd.innerHTML = "Listening your Voice ...";
      };
      recognizer.onspeechend = function () {
        stop.click();
      };
      recognizer.onresult = function (event) {
        var outText = event.results[0][0].transcript;
        var confidence = event.results[0][0].confidence * 100;
        output.value = outText;
        confd.innerHTML = "Confidence: " + Math.round(confidence) + "%";
      };
    </script>
  </body>
</html>
""")
