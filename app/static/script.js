$(document).ready(function() {
  // Get references to the text input and translation text area
  var textInput = $("#text_to_translate");
  var translationTextArea = $("#translated_textarea");

  // Add an event listener to the text input that listens for the "input" event
  textInput.on("input", function() {
    // Get the current text input and selected languages
    var textToTranslate = textInput.val();
    var textLanguage = $("#text_model").val();
    var translationLanguage = $("#translate_model").val();

    // Update the URL with the current input values
    window.history.replaceState(null, null, "/translate?text_to_translate=" + encodeURIComponent(textToTranslate) + "&text_model=" + encodeURIComponent(textLanguage) + "&translate_model=" + encodeURIComponent(translationLanguage));

    // Send an AJAX request to the server to get the translation
    $.ajax({
      type: "GET",
      url: "/translate",
      data: {
        text_to_translate: textToTranslate,
        text_model: textLanguage,
        translate_model: translationLanguage
      },
      success: function(data) {
        console.log(data);
        translationTextArea.text(data);
      },
      error: function() {
        // Handle the error
        translationTextArea.text("Sorry! Translation is not available for this pair!");
      }
    });
  });
});
