document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.getElementById("cep");
    const btnBuscar = document.getElementById("btnBuscarCep");
    const feedback = document.getElementById("cepFeedback");

    if (!cepInput || !btnBuscar) return;

    function buscarCep() {
        let cep = cepInput.value.replace(/\D/g, '');

        if (cep.length !== 8) {
            feedback.textContent = "CEP inválido. Digite 8 números.";
            feedback.className = "text-danger";
            return;
        }

        feedback.textContent = "Buscando endereço...";
        feedback.className = "text-muted";

        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(res => res.json())
            .then(data => {
                if (data.erro) {
                    feedback.textContent = "CEP não encontrado.";
                    feedback.className = "text-danger";
                    return;
                }

                document.getElementById("rua").value = data.logradouro;
                document.getElementById("bairro").value = data.bairro;
                document.getElementById("cidade").value = data.localidade;
                document.getElementById("estado").value = data.uf;

                feedback.textContent = "Endereço preenchido com sucesso.";
                feedback.className = "text-success";
            })
            .catch(() => {
                feedback.textContent = "Erro ao consultar o CEP.";
                feedback.className = "text-danger";
            });
    }

    btnBuscar.addEventListener("click", buscarCep);

    // Extra: permitir apertar Enter no campo CEP
    cepInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();
            buscarCep();
        }
    });
});
