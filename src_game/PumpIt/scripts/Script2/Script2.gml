
function bressenhams_line_algorithm(x1,y1,x2,y2,func) {
     
    // Differential
	var _points = [];
    var dx = x2-x1;
    var dy = y2-y1;
     
    // Increments
    var sx = sign(dx);
    var sy = sign(dy);
     
    // Segment Length
    dx = abs(dx);
    dy = abs(dy);
    var d = max(dx,dy);
     
    var r = d/2;
     
    if (dx > dy) {
        for (var i=0;i<d;i++) {
            array_push(_points, [x1, y1]);
            x1 += sx;
            r += dy;
            if (r >= dx) {
                y1 += sy;
                r -= dx;
            }
        }
    }
    else {
        for (var i=0;i<d;i++) {
            array_push(_points, [x1, y1]);
            y1 += sy;
            r += dx;
            if (r >= dy) {
                x1 += sx;
                r -= dy;
            }
        }
    }
	return _points;
}