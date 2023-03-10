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
        ["????????????", ["am-ET"]],
        ["Az??rbaycanca", ["az-AZ"]],
        ["???????????????", ["bn-BD", "????????????????????????"], ["bn-IN", "????????????"]],
        ["Bahasa Indonesia", ["id-ID"]],
        ["Bahasa Melayu", ["ms-MY"]],
        ["Catal??", ["ca-ES"]],
        ["??e??tina", ["cs-CZ"]],
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
          "Espa??ol",
          ["es-AR", "Argentina"],
          ["es-BO", "Bolivia"],
          ["es-CL", "Chile"],
          ["es-CO", "Colombia"],
          ["es-CR", "Costa Rica"],
          ["es-EC", "Ecuador"],
          ["es-SV", "El Salvador"],
          ["es-ES", "Espa??a"],
          ["es-US", "Estados Unidos"],
          ["es-GT", "Guatemala"],
          ["es-HN", "Honduras"],
          ["es-MX", "M??xico"],
          ["es-NI", "Nicaragua"],
          ["es-PA", "Panam??"],
          ["es-PY", "Paraguay"],
          ["es-PE", "Per??"],
          ["es-PR", "Puerto Rico"],
          ["es-DO", "Rep??blica Dominicana"],
          ["es-UY", "Uruguay"],
          ["es-VE", "Venezuela"],
        ],
        ["Euskara", ["eu-ES"]],
        ["Filipino", ["fil-PH"]],
        ["Fran??ais", ["fr-FR"]],
        ["Basa Jawa", ["jv-ID"]],
        ["Galego", ["gl-ES"]],
        ["?????????????????????", ["gu-IN"]],
        ["Hrvatski", ["hr-HR"]],
        ["IsiZulu", ["zu-ZA"]],
        ["??slenska", ["is-IS"]],
        ["Italiano", ["it-IT", "Italia"], ["it-CH", "Svizzera"]],
        ["???????????????", ["kn-IN"]],
        ["???????????????????????????", ["km-KH"]],
        ["Latvie??u", ["lv-LV"]],
        ["Lietuvi??", ["lt-LT"]],
        ["??????????????????", ["ml-IN"]],
        ["???????????????", ["mr-IN"]],
        ["Magyar", ["hu-HU"]],
        ["?????????", ["lo-LA"]],
        ["Nederlands", ["nl-NL"]],
        ["?????????????????? ????????????", ["ne-NP"]],
        ["Norsk bokm??l", ["nb-NO"]],
        ["Polski", ["pl-PL"]],
        ["Portugu??s", ["pt-BR", "Brasil"], ["pt-PT", "Portugal"]],
        ["Rom??n??", ["ro-RO"]],
        ["???????????????", ["si-LK"]],
        ["Sloven????ina", ["sl-SI"]],
        ["Basa Sunda", ["su-ID"]],
        ["Sloven??ina", ["sk-SK"]],
        ["Suomi", ["fi-FI"]],
        ["Svenska", ["sv-SE"]],
        ["Kiswahili", ["sw-TZ", "Tanzania"], ["sw-KE", "Kenya"]],
        ["?????????????????????", ["ka-GE"]],
        ["??????????????", ["hy-AM"]],
        [
          "???????????????",
          ["ta-IN", "?????????????????????"],
          ["ta-SG", "?????????????????????????????????"],
          ["ta-LK", "??????????????????"],
          ["ta-MY", "?????????????????????"],
        ],
        ["??????????????????", ["te-IN"]],
        ["Ti???ng Vi???t", ["vi-VN"]],
        ["T??rk??e", ["tr-TR"]],
        ["????????????", ["ur-PK", "??????????????"], ["ur-IN", "??????????"]],
        ["????????????????", ["el-GR"]],
        ["??????????????????", ["bg-BG"]],
        ["P????????????", ["ru-RU"]],
        ["????????????", ["sr-RS"]],
        ["????????????????????", ["uk-UA"]],
        ["?????????", ["ko-KR"]],
        [
          "??????",
          ["cmn-Hans-CN", "????????? (????????????)"],
          ["cmn-Hans-HK", "????????? (??????)"],
          ["cmn-Hant-TW", "?????? (??????)"],
          ["yue-Hant-HK", "?????? (??????)"],
        ],
        ["?????????", ["ja-JP"]],
        ["??????????????????", ["hi-IN"]],
        ["?????????????????????", ["th-TH"]],
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
