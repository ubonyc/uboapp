
    function ratingcalc(one, two, three, four, five)
    {
        var rating = one * 1 + two * 2 + three * 3 + four * 4 + five * 5;
        var ratingfactor =  +one + +two + +three + +four + +five;
        return(rating/ratingfactor);
    }


