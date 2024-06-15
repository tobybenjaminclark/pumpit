// Key Pressed Event
if (is_active) {
    // Handle text input
    var key = keyboard_string;
    if (key != "") {
        input_text += key;
        // Limit input length
        if (string_length(input_text) > max_length) {
            input_text = string_copy(input_text, 1, max_length);
        }
    }

    // Handle backspace
    if (keyboard_check_pressed(vk_backspace) && string_length(input_text) > 0) {
        input_text = "";
    }

    // Handle enter key (you can customize this part)
    if (keyboard_check_pressed(vk_enter)) {
        is_active = false;
    }
	keyboard_string = "";
}

global.input_text = input_text;
