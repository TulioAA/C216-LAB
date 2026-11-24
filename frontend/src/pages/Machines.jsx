import { useEffect, useState } from "react";
import api from "../services/api";

function Machines() {
  const [machines, setMachines] = useState([]);

  const [form, setForm] = useState({
    nome_maquina: "",
    marca: "",
    modelo: "",
    ano: "",
    horas_trabalhadas: "",
    horas_proxima_manutencao: "",
  });

  const [editingId, setEditingId] = useState(null);

  async function loadMachines() {
    const response = await api.get("/maquinas/");

    setMachines(response.data);
  }

  useEffect(() => {
    loadMachines();
  }, []);

  async function handleSubmit(e) {
    e.preventDefault();

    const payload = {
      ...form,
      ano: Number(form.ano),
      horas_trabalhadas: Number(
        form.horas_trabalhadas
      ),
      horas_proxima_manutencao: Number(
        form.horas_proxima_manutencao
      ),
    };

    if (editingId) {
      await api.put(
        `/maquinas/${editingId}`,
        payload
      );
    } else {
      await api.post(
        "/maquinas/",
        payload
      );
    }

    setForm({
      nome_maquina: "",
      marca: "",
      modelo: "",
      ano: "",
      horas_trabalhadas: "",
      horas_proxima_manutencao: "",
    });

    setEditingId(null);

    loadMachines();
  }

  async function deleteMachine(id) {
    await api.delete(
      `/maquinas/${id}`
    );

    loadMachines();
  }

  function editMachine(machine) {
    setEditingId(machine.id);

    setForm({
      nome_maquina:
        machine.nome_maquina,
      marca: machine.marca,
      modelo: machine.modelo,
      ano: machine.ano,
      horas_trabalhadas:
        machine.horas_trabalhadas,
      horas_proxima_manutencao:
        machine.horas_proxima_manutencao,
    });
  }

  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "0 auto",
        padding: "20px",
      }}
    >
      <h1>AgroManutenção </h1>

      <h2>
        Total de máquinas:
        {" "}
        {machines.length}
      </h2>

      <form
        onSubmit={handleSubmit}
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          marginBottom: "30px",
        }}
      >
        <input
          placeholder="Nome"
          value={form.nome_maquina}
          onChange={(e) =>
            setForm({
              ...form,
              nome_maquina:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Marca"
          value={form.marca}
          onChange={(e) =>
            setForm({
              ...form,
              marca:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Modelo"
          value={form.modelo}
          onChange={(e) =>
            setForm({
              ...form,
              modelo:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Ano"
          value={form.ano}
          onChange={(e) =>
            setForm({
              ...form,
              ano:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Horas Trabalhadas"
          value={
            form.horas_trabalhadas
          }
          onChange={(e) =>
            setForm({
              ...form,
              horas_trabalhadas:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Próxima Manutenção"
          value={
            form.horas_proxima_manutencao
          }
          onChange={(e) =>
            setForm({
              ...form,
              horas_proxima_manutencao:
                e.target.value,
            })
          }
        />

        <button type="submit">
          {editingId
            ? "Atualizar Máquina"
            : "Cadastrar Máquina"}
        </button>
      </form>

      {machines.map((machine) => (
        <div
          key={machine.id}
          style={{
            border:
              "1px solid #ccc",
            borderRadius: "10px",
            padding: "15px",
            marginBottom: "15px",
          }}
        >
          <h3>
            {machine.nome_maquina}
          </h3>

          <p>
            Marca:
            {" "}
            {machine.marca}
          </p>

          <p>
            Modelo:
            {" "}
            {machine.modelo}
          </p>

          <p>
            Ano:
            {" "}
            {machine.ano}
          </p>

          <p>
            Horas Trabalhadas:
            {" "}
            {machine.horas_trabalhadas}
          </p>

          <p>
            Próxima Manutenção:
            {" "}
            {
              machine.horas_proxima_manutencao
            }
          </p>

          <p>
            Manutenção atrasada:
            {" "}
            {machine.manutencao_atrasada
              ? "Sim"
              : "Não"}
          </p>

          <button
            onClick={() =>
              editMachine(machine)
            }
          >
            Editar
          </button>

          <button
            onClick={() =>
              deleteMachine(
                machine.id
              )
            }
            style={{
              marginLeft: "10px",
            }}
          >
            Excluir
          </button>
        </div>
      ))}
    </div>
  );
}

export default Machines;