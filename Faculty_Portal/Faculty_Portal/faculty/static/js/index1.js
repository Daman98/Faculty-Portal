$(function() {
	// Time wasted here: 3 hours

	// For card rotation
	$(".btn-rotate").click(function() {
		// Long explanation: The button that is clicked, will have its grand parent add a class to its child. The main reason I couldn't use .parent() was that it gets the closest positioned parent, either relative or absolute. The problem was that the card-front got the .rotate-container as its parent, but the card-back was being the closest positioned element as the parent of the button. In order to circumvent this I either needed to use 3 offsetparent() and have really messy code, or just use the .closest() which as its name suggests gets the closest named or unnamed element. So in the end, I get the grand parent of the button which is the .rotate container and I find its children which are the .card-front and .card-back and toggle the rotation classes on them. Also if I didn't specify which button's ancestor would assign the class, whenever any btn-rotate button is clicked, all three cards would rotate at once which makes for a funny yet unhelpful design.
		var $parent = $(this).closest(".rotate-container");

		// Probably easier to use an id, but I made it work
		$parent.children(".card-front").toggleClass(" rotate-card-front");
		$parent.children(".card-back").toggleClass(" rotate-card-back");
	});
});