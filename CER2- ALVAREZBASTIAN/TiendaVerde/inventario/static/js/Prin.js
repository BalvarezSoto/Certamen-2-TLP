document.addEventListener('DOMContentLoaded', function () {
    const selectMaterial = document.querySelectorAll('select')[0];
    const selectSubtipo = document.querySelectorAll('select')[1];
    const nombreInput = document.getElementById('exname');
    const correoInput = document.getElementById('exampleFormControlInput1');
    const direccionInput = document.getElementById('inputAddress');
    const textareaInput = document.getElementById('exampleFormControlTextarea1');
    const submitButton = document.querySelector('.btn-primary');

    // Opciones para el segundo select dependiendo de la opción seleccionada en el primer select
    const opciones = {
        1: ["Botellas", "Bolsas", "Envases"],
        2: ["Periódicos", "Cartón", "Papel de Oficina"],
        3: ["Botellas", "Frascos", "Cristaleria"],
        4: ["Latas", "Cables", "Electrodomesticos pequeños"],
        5: ["Componentes de Computadoras", "Teléfonos", "Baterías"]
    };

    // Función que actualiza las opciones del segundo select
    function actualizarOpciones() {
        selectSubtipo.innerHTML = '';
        const seleccion = selectMaterial.value;

        // Si el valor existe en las opciones, agregamos las nuevas opciones al segundo select
        if (opciones[seleccion]) {
            opciones[seleccion].forEach(function (subtipo) {
                const option = document.createElement('option');
                option.value = subtipo;
                option.text = subtipo;
                selectSubtipo.add(option);
            });
        } else {
            const option = document.createElement('option');
            option.text = "Selecciona un material primero";
            selectSubtipo.add(option);
        }
    }

    // Validaciones de los campos del formulario
    function validarFormulario() {
        let esValido = true;
        const Correo = /^[^\s@]+@[^\s@]+\.[a-z]{2,3}$/;

        if (nombreInput.value.trim() === '') {
            alert("Por favor, ingresa un nombre.");
            esValido = false;
        }

        if (!Correo.test(correoInput.value)) {
            alert("Por favor, ingresa un correo electrónico válido.");
            esValido = false;
        }

        if (direccionInput.value.trim() === '') {
            alert("Por favor, ingresa una dirección.");
            esValido = false;
        }

        return esValido;
    }

    // Función para limpiar el formulario
    function limpiarFormulario() {
        if (confirm("¿Enviar solicitud?")) {
            nombreInput.value = '';
            correoInput.value = '';
            direccionInput.value = '';
            textareaInput.value = '';
            selectMaterial.value = ''; 
            actualizarOpciones();
            alert("Se ha enviado la solicitud con exito.");
        }
    }

    selectMaterial.addEventListener('change', actualizarOpciones);

    submitButton.addEventListener('click', function (e) {
        e.preventDefault();

        if (validarFormulario()) {
            limpiarFormulario();
        }
    });
    actualizarOpciones();
});