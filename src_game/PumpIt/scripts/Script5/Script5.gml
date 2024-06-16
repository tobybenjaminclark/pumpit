// Define the color interpolation function
function interpolate_color(val, min_val, max_val, color1, color2) {
    // Clamp the value to be within the specified range
    var clamped_val = clamp(val, min_val, max_val);

    // Normalize the value to a range of 0 to 1
    var normalized_val = (clamped_val - min_val) / (max_val - min_val);

    // Get the RGB components of the two colors
    var r1 = color_get_red(color1);
    var g1 = color_get_green(color1);
    var b1 = color_get_blue(color1);
    
    var r2 = color_get_red(color2);
    var g2 = color_get_green(color2);
    var b2 = color_get_blue(color2);

    // Interpolate each color component
    var r = lerp(r1, r2, normalized_val);
    var g = lerp(g1, g2, normalized_val);
    var b = lerp(b1, b2, normalized_val);

    // Combine the interpolated components into a single color
    return make_color_rgb(r, g, b);
}