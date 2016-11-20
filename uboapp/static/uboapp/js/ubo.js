
    function ratingcalc(one, two, three, four, five)
    {
        var rating = one * 1 + two * 2 + three * 3 + four * 4 + five * 5;
        var ratingfactor =  +one + +two + +three + +four + +five;
        return(rating/ratingfactor);
    }

    function ratingscount(one, two, three, four, five)
    {
        var ratingfactor =  +one + +two + +three + +four + +five;
        return(ratingfactor);
    }



        var activebuilding;

        function slideshow(){
        blueimp.Gallery(
            [
                {
                    data: {urls: ['media/111_Kent_1.jpeg']}
                },
                {
                    data: {urls: ['media/111_Kent_2.jpeg']}
                }
            ],
            {
                urlProperty: 'data.urls[0]'
            }
        );
        }


