	function opengallery(street,number,year,stories,units,rating,ratingscount,buildingtype,area,lotsize,marketvalue,image,five,four,three,two,one){

	            document.getElementById("galleryfront").src = image;

                document.getElementById("street").innerHTML = number + ' ' + street;
                document.getElementById("year").innerHTML = year;
                document.getElementById("stories").innerHTML = stories;
                document.getElementById("units").innerHTML = units;
                document.getElementById("buildingclass").innerHTML = buildingtype.toUpperCase();
                document.getElementById("area").innerHTML = area + " SQFT";
                document.getElementById("lotsize").innerHTML = lotsize + " SQFT";

                var amount = parseFloat(marketvalue);
                document.getElementById("marketvalue").innerHTML = "$" + amount.toLocaleString();
                document.getElementById("ratingscount").innerHTML = ratingscount;
                document.getElementById("rating_image").src = "static/uboapp/stars/stars_00.png";


                rating_show(rating);

                var rating_max = Math.max(one,two,three,four,five);

                document.getElementById("rating_five").style.width = five/rating_max*150;
                document.getElementById("rating_four").style.width = four/rating_max*150;
                document.getElementById("rating_three").style.width = three/rating_max*150;
                document.getElementById("rating_two").style.width = two/rating_max*150;
                document.getElementById("rating_one").style.width = one/rating_max*150;

                document.getElementById("rating_digits").innerHTML = rating.toFixed(1);

                if (rating <= 1.5) { document.getElementById("rating_label").innerHTML = "ACCEPTABLE"; }
                if ((rating >= 1.5) && (rating <= 2.5)) { document.getElementById("rating_label").innerHTML = "SHOWS SIGNS OF UGLINESS"; }
                if ((rating >= 2.5) && (rating <= 3.5)) { document.getElementById("rating_label").innerHTML = "EYE SORE"; }
                if ((rating >= 3.5) && (rating <= 4.5)) { document.getElementById("rating_label").innerHTML = "OFFENSIVE"; }
                if (rating >= 4.5) { document.getElementById("rating_label").innerHTML = "TRULY UGLY&#8482"; }

                document.getElementById("content-div").style.display = 'inline';
                document.getElementById("content-div").style.visibility = 'visible';

                document.getElementById("init_div").style.display = 'none';
                document.getElementById("init_div").style.visibility = 'visible';


    }




	function rating_show(rating_grade){

	if ((rating_grade >= 0) && (rating_grade <= 0.5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_00.png"; } 
	if ((rating_grade >= 0.5) && (rating_grade <= 1)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_05.png"; } 
	if ((rating_grade >= 1) && (rating_grade <= 1.5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_10.png"; } 
	if ((rating_grade >= 1.5) && (rating_grade <= 2)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_15.png"; } 
    if ((rating_grade >= 2) && (rating_grade <= 2.5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_20.png"; }  
	if ((rating_grade >= 2.5) && (rating_grade <= 3)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_25.png"; } 
	if ((rating_grade >= 3) && (rating_grade <= 3.5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_30.png"; } 
	if ((rating_grade >= 3.5) && (rating_grade <= 4)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_35.png"; } 
	if ((rating_grade >= 4) && (rating_grade <= 4.5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_40.png"; } 
	if ((rating_grade >= 4.5) && (rating_grade <= 5)) { document.getElementById("rating_image").src = "static/uboapp/stars/stars_45.png"; }  

	}


