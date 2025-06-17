const joystick = document.querySelector(".joystick");
const joystickWrapper = document.querySelector(".joystick-wrapper");
let joystickWrapperRect = joystickWrapper.getBoundingClientRect();
let is_mouse_down = false;
let joystickPosition = [0, 0];

addEventListener("resize", () => {
	joystickWrapperRect = joystickWrapper.getBoundingClientRect();
});

const updateJoystick = event => {
	if (event.target != joystickWrapper || !is_mouse_down) {
		joystick.style.transform = '';
		joystickPosition = [0, 0];
	joystick.classList.add("unactive");
		return
	}
	joystick.classList.remove("unactive");

	if (event.type.includes("mouse")) {
		joystickPosition = [event.clientX - joystickWrapperRect.left - joystickWrapperRect.width / 2,
			event.clientY - joystickWrapperRect.top - joystickWrapperRect.height / 2];
	} else if (event.type.includes("touch")) {
		joystickPosition = [event.touches[0].clientX - joystickWrapperRect.left - joystickWrapperRect.width / 2,
			event.touches[0].clientY - joystickWrapperRect.top - joystickWrapperRect.height / 2]
	} else {
		alert("Unsupported interaction")
	}

	joystick.style.transform = `translate(${joystickPosition[0]}px, ${joystickPosition[1]}px)`;

};

const onMouseDown = event => {
	if (event.button !== 0) {return}
	is_mouse_down = true;
	updateJoystick(event);
};

const onMouseUp = event => {
	if (typeof event.button !== 'undefined' && event.button !== 0) {return}
	is_mouse_down = false;
	updateJoystick(event);
};

document.addEventListener("mousedown", onMouseDown);
document.addEventListener("mouseup", onMouseUp);
joystickWrapper.addEventListener("mousemove", updateJoystick);

document.addEventListener("touchend", onMouseUp);
joystickWrapper.addEventListener("touchmove", event => {
	is_mouse_down = true;
	updateJoystick(event);
});

document.querySelector("button.left").addEventListener("click", () => {
	socket.emit("JoystickController.left-click");
});

document.querySelector("button.right").addEventListener("click", () => {
	socket.emit("JoystickController.right-click");
});

const textInput = document.querySelector(".virtual-keyboard input");
document.querySelector(".virtual-keyboard button.send").addEventListener("click", () => {
	socket.emit("JoystickController.text-input", textInput.value);
	textInput.value = '';
});

document.querySelector(".virtual-keyboard button.backspace").addEventListener("click", () => {
	socket.emit("JoystickController.backspace");
});

document.querySelector(".virtual-keyboard button.enter").addEventListener("click", () => {
	socket.emit("JoystickController.enter");
});

const scrollBar = document.querySelector(".scroll-bar input");
const scrollBarReset = () => {
	scrollBar.value = 0;

	// Re-render the range input on firefox
	scrollBar.setAttribute('type', '');
	scrollBar.setAttribute('type', 'range');

};

scrollBarReset(); // Not always at 0 because of the cache
scrollBar.addEventListener("mouseup", scrollBarReset);
scrollBar.addEventListener("touchend", scrollBarReset);


setInterval(() => {

	const joystickRange = [joystickPosition[0] / (joystickWrapperRect.width / 2), 
		joystickPosition[1] / (joystickWrapperRect.height / 2)];

	if (joystickRange[0] !== 0 && joystickRange[1] !== 0) {
		socket.emit("JoystickController.move-mouse", joystickRange);
	}

	if (scrollBar.value) {
		socket.emit("JoystickController.scroll", scrollBar.value);
	}

}, 100);

