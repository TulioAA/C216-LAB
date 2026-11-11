import { useEffect, useState } from "react";
import api from "../services/api";

function Maintenances() {
  const [maintenances, setMaintenances] = useState([]);

  const [form, setForm] = useState({
    maquina_id: "",
    tipo_manutencao: "",
    descricao: "",
    data_manutencao: "",
    custo: "",
  });

  const [editingId, setEditingId] = useState(null);

  async function loadMaintenances() {
    const response = await api.get(
      "/manutencoes/"
    );

    setMaintenances(response.data);
  }

  useEffect(() => {
    loadMaintenances();
  }, []);

  async function handleSubmit(e) {
    e.preventDefault();

    const payload = {
      ...form,
      maquina_id: Number(form.maquina_id),
      custo: Number(form.custo),
    };

    if (editingId) {
      await api.put(
        `/manutencoes/${editingId}`,
        payload
      );
    } else {
      await api.post(
        "/manutencoes/",
        payload
      );
    }

    setForm({
      maquina_id: "",
      tipo_manutencao: "",
      descricao: "",
      data_manutencao: "",
      custo: "",
    });

    setEditingId(null);

    loadMaintenances();
  }

  async function deleteMaintenance(id) {
    await api.delete(
      `/manutencoes/${id}`
    );

    loadMaintenances();
  }

  function editMaintenance(
    maintenance
  ) {
    setEditingId(
      maintenance.id
    );

    setForm({
      maquina_id:
        maintenance.maquina_id,
      tipo_manutencao:
        maintenance.tipo_manutencao,
      descricao:
        maintenance.descricao,
      data_manutencao:
        maintenance.data_manutencao,
      custo:
        maintenance.custo,
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
      <h1>Manutenções</h1>

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
          placeholder="ID Máquina"
          value={form.maquina_id}
          onChange={(e) =>
            setForm({
              ...form,
              maquina_id:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Tipo"
          value={
            form.tipo_manutencao
          }
          onChange={(e) =>
            setForm({
              ...form,
              tipo_manutencao:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Descrição"
          value={form.descricao}
          onChange={(e) =>
            setForm({
              ...form,
              descricao:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Data"
          value={
            form.data_manutencao
          }
          onChange={(e) =>
            setForm({
              ...form,
              data_manutencao:
                e.target.value,
            })
          }
        />

        <input
          placeholder="Custo"
          value={form.custo}
          onChange={(e) =>
            setForm({
              ...form,
              custo:
                e.target.value,
            })
          }
        />

        <button type="submit">
          {editingId
            ? "Atualizar"
            : "Cadastrar"}
        </button>
      </form>

      {maintenances.map(
        (maintenance) => (
          <div
            key={maintenance.id}
            style={{
              border:
                "1px solid #ccc",
              padding: "15px",
              borderRadius:
                "10px",
              marginBottom:
                "15px",
            }}
          >
            <h3>
              {
                maintenance.tipo_manutencao
              }
            </h3>

            <p>
              Máquina:
              {" "}
              {
                maintenance.maquina_id
              }
            </p>

            <p>
              Descrição:
              {" "}
              {
                maintenance.descricao
              }
            </p>

            <p>
              Data:
              {" "}
              {
                maintenance.data_manutencao
              }
            </p>

            <p>
              Custo:
              {" "}
              R$
              {maintenance.custo}
            </p>

            <button
              onClick={() =>
                editMaintenance(
                  maintenance
                )
              }
            >
              Editar
            </button>

            <button
              style={{
                marginLeft:
                  "10px",
              }}
              onClick={() =>
                deleteMaintenance(
                  maintenance.id
                )
              }
            >
              Excluir
            </button>
          </div>
        )
      )}
    </div>
  );
}

export default Maintenances;