var modalcontent;

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}





// Submit post on submit
$('#rating-form').on('submit', function(event){
    event.preventDefault();
    console.log("post_rating : Form submitted");  // sanity check
    post_rating();
});

// AJAX for posting rating
function post_rating() {
    console.log("post_rating : Function called"); // sanity check
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
    //console.log("post_rating : ajax setup completed"); // sanity check
    //console.log("post_rating : post-rate : " + $(":input[name=rateradio]:checked").val()); // sanity check

    $.ajax({
        url : "post_rating/", // the endpoint
        type : "POST", // http method
        data : { the_post : $(":input[name=rateradio]:checked").val(), active_building : activebuilding }, // data sent with the post request

        //data : { the_post : $('#post-rate').val() }, // data sent with the post request



        // handle a successful response
        success : function(json) {
            $('#post_rate').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console

            //console.log("post_rating : success"); // another sanity check
            console.log("TRANSITION");
            get_building(activebuilding);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};



// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// AJAX for posting comment
function create_post() {
    console.log("create post is working!"); // sanity check
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
    console.log("ajax setup completed"); // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


// AJAX for getting
function get_building(building_id) {
    console.log("get_building : ajax called / building_id : " + building_id); // sanity check
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
    //console.log("get_building : ajax setup completed"); // sanity check
    //console.log("get_building : ID = " + building_id)

    $.ajax({
        url : "get_building/", // the endpoint
        type : "GET", // http method
        data : { the_post : building_id }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("get_building : success"); // another sanity check
            document.getElementById("street").innerHTML = json.streetnumber + ' ' + json.streetname;
            document.getElementById("building_class").innerHTML = json.building_class;
            document.getElementById("year_built").innerHTML = json.year_built;
            document.getElementById("stories").innerHTML = json.stories;
            document.getElementById("res_units").innerHTML = json.res_units;
            document.getElementById("com_units").innerHTML = json.com_units;
            document.getElementById("structure_type").innerHTML = json.structure_type;
            document.getElementById("grade").innerHTML = json.grade;
            document.getElementById("construction_type").innerHTML = json.construction_type;

            temp = parseFloat(json.area);
            document.getElementById("area").innerHTML = temp.toLocaleString();

            temp = parseFloat(json.lotsize);
            document.getElementById("lotsize").innerHTML = temp.toLocaleString();

            temp = parseFloat(json.marketvalue);
            document.getElementById("marketvalue").innerHTML = "$" + temp.toLocaleString();

            document.getElementById("ratings_count").innerHTML = json.ratings_count;

            rate_digits = json.ratings_rate.rate__avg.toFixed(1);

            //console.log("rate digits : " + rate_digits); // sanity check

            document.getElementById("rating_digits").innerHTML = rate_digits;

            rating_show(rate_digits);

            var rating_max = Math.max(json.ratings_one,json.ratings_two,json.ratings_three,json.ratings_four,json.ratings_five);

                var max_width = document.getElementById("rating_width").offsetWidth - 30;

                document.getElementById("rating_five").style.width = json.ratings_five/rating_max*max_width;
                document.getElementById("rating_four").style.width = json.ratings_four/rating_max*max_width;
                document.getElementById("rating_three").style.width = json.ratings_three/rating_max*max_width;
                document.getElementById("rating_two").style.width = json.ratings_two/rating_max*max_width;
                document.getElementById("rating_one").style.width = json.ratings_one/rating_max*max_width;

                if (rate_digits <= 1.5) { document.getElementById("rating_label").innerHTML = "ACCEPTABLE"; }
                if ((rate_digits >= 1.5) && (rate_digits <= 2.5)) { document.getElementById("rating_label").innerHTML = "SHOWS SIGNS OF UGLINESS"; }
                if ((rate_digits >= 2.5) && (rate_digits <= 3.5)) { document.getElementById("rating_label").innerHTML = "EYE SORE"; }
                if ((rate_digits >= 3.5) && (rate_digits <= 4.5)) { document.getElementById("rating_label").innerHTML = "OFFENSIVE"; }
                if (rate_digits >= 4.5) { document.getElementById("rating_label").innerHTML = "TRULY UGLY&#8482"; }





                modalcontent = "<p>ADDRESS : " + json.streetnumber + " " + json.streetname + "</p>" +
                    "<p>CLASS : " + json.building_class.toUpperCase() + "</p>" +
                    "<p>YEAR COMPLETED : " + json.year_built + "</p>" +
                    "<p>STORIES : " + json.stories + "</p>" +
                    "<p>RESIDENTIAL UNITS : " + json.res_units + "</p>" +
                    "<p>COMMERCIAL UNITS : " + json.com_units + "</p>" +
                    "<p>STRUCTURE TYPE : " + json.structure_type.toUpperCase() + "</p>" +
                    "<p>GRADE : " + json.grade + "</p>" +
                    "<p>CONSTRUCTION TYPE : " + json.construction_type.toUpperCase() + "</p>" +
                    "<p>AREA : " + parseFloat(json.area).toLocaleString() + " SQFT</p>" +
                    "<p>LOT SIZE : " + parseFloat(json.lotsize).toLocaleString() + " SQFT</p>" +
                    "<p>MARKET VALUE : $" + parseFloat(json.marketvalue).toLocaleString() + "</p>";

        },


        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};




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



	function overlay(){

        console.log('allo');

        var modalheight = 380;
        var modalwidth = 250;
        //modalcontent = "yes papa";

                $("#details").html(modalcontent);
                $("#details").dialog(
                    {width: modalwidth},
                    {height: modalheight}
                );
    };


    function moredetails(){
        //document.getElementById("data_id").style.height = 500;

        document.getElementById("hidden_div").style.visibility = "visible";
        document.getElementById("hidden_div").style.display = "inline";
        document.getElementById("more_div").innerHTML = '<a href="javascript:lessdetails()">Less details</a>';

    }

    function lessdetails(){
        document.getElementById("hidden_div").style.visibility = "hidden";
        document.getElementById("hidden_div").style.display = "none";
        document.getElementById("more_div").innerHTML = '<a href="javascript:moredetails()">More details</a>';

    }