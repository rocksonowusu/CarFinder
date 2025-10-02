document.addEventListener('DOMContentLoaded', function(){
    const modal = document.getElementById('recommendModal');
    const startButton = document.getElementById("startButton");
    const closeBtn = document.querySelector(".close");
    const form = document.getElementById("recommendForm");
    const steps = document.querySelectorAll(".form-step");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const submitButton = document.getElementById("submitButton");
    const progressFill = document.getElementById("progressFill");
    const currentStepText = document.getElementById("currentStep");

    let currentStep = 1;
    const totalSteps = steps.length;

    //Open Modal
    startButton.addEventListener('click', function(){
        modal.style.display = 'block';
        
    }); 

    //Close Modal
    closeBtn.addEventListener('click', closeModal)
    window.addEventListener('click', function(e){
        if (e.target === modal ){
            closeModal();
        }
    });

    function closeModal(){
        modal.style.display = 'none';
        resetForm();
    }

    function resetForm(){
        currentStep = 1;
        form.reset();
        showStep(currentStep);
    }

    //Show specific step
    function showStep(step){
        steps.forEach((s, index)=>{
            s.classList.remove('active');
            if (index + 1 === step) {
                s.classList.add('active');
            }
        });

        //Update Progress
        const progress = (step / totalSteps) * 100;
        progressFill.style.width = progress + '%';
        currentStepText.textContent = step;

        //Button Visibilty
        prevButton.style.display = step === 1 ? 'none' : 'inline-block';
        nextButton.style.display = step === totalSteps ? 'none' : 'inline-block';
        submitButton.style.display = step === totalSteps ? 'inline-block' : 'none';
    }

    // Next Button
    nextButton.addEventListener('click', function(){
        if (validateStep(currentStep)){
            currentStep++;
            showStep(currentStep);
        }
    });

    // Previous Button
    prevButton.addEventListener('click', function(){
        currentStep--;
        showStep(currentStep);
    });

    // Validate current step
    function validateStep(step) {
        const currentStepElement = document.querySelector(`.form-step[data-step="${step}"]`);
        const inputs = currentStepElement.querySelectorAll('input[type="radio"]');
        const isChecked = Array.from(inputs).some(input => input.checked);

        if (!isChecked){
            alert('Please select an option before continuing.');
            return false;
        }
        return true;
    }

    // Form submission validation
    form.addEventListener('submit', function(e){
        if (!validateStep(currentStep)){
            e.preventDefault();
        }
    });

    //Initialize
    showStep(currentStep);
})