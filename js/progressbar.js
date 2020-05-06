class ProgressBar{
	constructor(element, intial_value){
		this.value_elem = element.querySelector('.result');
		this.fill_elem = element.querySelector('.progress-bar-fill');
		this.base_title = document.title;
		this.set_value(intial_value);
	}

	set_value(new_value){
		this.value_scaled = new_value * 0.25; //100% of the bar is actually 400cm, scaled for better visibility
	this.value = new_value;

		if (this.value_scaled < 0) {
			this.value_scaled = 0;
		}

		if (this.value_scaled > 100) {
			this.value_scaled = 100;
		}

		
		this.update();
	}

	update(){
		const percentage = this.value_scaled + '%';

		this.fill_elem.style.width = percentage;
		this.value_elem.textContent = this.value + 'cm';

		//updating browser tab
		document.title = "(" + this.value + ") " + this.base_title;

	}
}