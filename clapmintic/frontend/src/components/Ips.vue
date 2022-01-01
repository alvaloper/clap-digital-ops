<template>

    <div class="signUp_ips">
        <div class="container_signUp_ips">
            <h2>Registrar IPS</h2>

            <form v-on:submit.prevent="processSignUp" >
                <input type="text" v-model="ips.id_reps" placeholder="ID">
                <br>
                
                <input type="text" v-model="ips.nombre" placeholder="Nombre">
                <br>
                
                <input type="text" v-model="ips.tipo_de_entidad" placeholder="Tipo">
                <br>

                <input type="text" v-model="ips.representante" placeholder="Representante">
                <br>

                <input type="text" v-model="ips.nivel_de_atencion" placeholder="Nivel">
                <br>

                <button type="submit">Guardar IPS</button>
            </form>
        </div>
    
        <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                    <tr>
                      <th>ID REPS</th>
                      <th>NOMBRE</th>
                      <th>TIPO DE ENTIDAD</th>
                      <th>REPRESENTANTE</th>
                      <th>NIVEL DE ATENCIÓN</th>
                      <th>ACCIONES</th>
                    </tr>
            </thead>
            <tbody>
                    <tr v-for="ips in ips_data">
                      <td>{{ ips.id_reps }}</td>
                      <td>{{ ips.nombre }}</td>
                      <td>{{ ips.tipo_de_entidad }}</td>
                      <td>{{ ips.representante }}</td>
                      <td>{{ ips.nivel_de_atencion }}</td>
                      <td><button class="btn btn-sm btn-success" v-on:click="populatePostToEdit(ips)">Editar</button></td>
                      <!-- <td><button class="btn btn-sm btn-danger" >DELETE</button></td> -->

                      <td><button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(ips)"> Eliminar
                      </button></td>          
                      <td><button class="btn btn-sm btn-info" v-on:click="updateedit(ips)"> Actualizar
                      </button></td>
                    </tr>
        </tbody>
        </table>
        </div>
        
    </div>

    

</template>




<script>
import axios from 'axios';
import jwt_decode from "jwt-decode";
export default {
    name: "Ips",
    data: function(){
        return {
            ips_data: {},
            ips: {
                // ips_data: [],
                ips_reps: "",
                nombre: "",
                tipo_de_entidad: "",
                representante: "",
                nivel_de_atencion: ""
            }
        }
    },
    methods: {
        
        processSignUp: function(){
            axios.post(
                "http://127.0.0.1:8000/ips/", 
                this.ips,  
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        id_reps: this.ips.id_reps,
                        nombre: this.ips.nombre,
                        tipo_de_entidad: this.ips.tipo_de_entidad,
                        representante: this.ips.representante,
                        nivel_de_atencion: this.ips.nivel_de_atencion,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    axios.get('http://127.0.0.1:8000/ips/')
                    .then( response => {
                        this.ips_data = response.data
                        console.log(this.ips_data)
                    })

                    this.$emit('completedSignUp', dataSignUp)
                    this.ips.id_reps = ""
                    this.ips.nombre = ""
                    this.ips.tipo_de_entidad = ""
                    this.ips.representante = ""
                    this.ips.nivel_de_atencion = ""
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");  
                });
        },
        all: function () {
        axios.get('http://127.0.0.1:8000/ips/')
            .then( response => {
                this.ips_data = response.data
            });
        },
        deleteSubscription: function(ips) {
            if (confirm('Delete ' + ips.nombre)) {
                axios.delete(`http://127.0.0.1:8000/ips/${ips.id_reps}/`)
                    .then( response => {
                        this.all();
                    });
            }
        },
        populatePostToEdit(ips) {
            // this.model = Object.assign({}, ips)
            this.ips.id_reps=ips.id_reps;
            this.ips.nombre=ips.nombre;
            this.ips.tipo_de_entidad=ips.tipo_de_entidad;
            this.ips.representante=ips.representante;
            this.ips.nivel_de_atencion=ips.nivel_de_atencion;
        },
        updateedit: function (ips) {
        axios.put(`http://127.0.0.1:8000/ips/${ips.id_reps}/`,
                {
                    id_reps: this.ips.id_reps,
                    nombre: this.ips.nombre,
                    tipo_de_entidad: this.ips.tipo_de_entidad,
                    representante: this.ips.representante,
                    nivel_de_atencion: this.ips.nivel_de_atencion,
                })
            
            // .then( response => {
            //     this.refreshData();
            //     // alert(response.data);
            //     alert("Registro Actualizado"); 
            //     // this.ips.id_reps = ""
            //     // this.ips.nombre = ""
            //     // this.ips.tipo_de_entidad = ""
            //     // this.ips.representante = ""
            //     // this.ips.nivel_de_atencion = ""
            // });

                .then((result) => {
                    alert("Registro Actualizado"); 
                    this.ips.id_reps = ""
                    this.ips.nombre = ""
                    this.ips.tipo_de_entidad = ""
                    this.ips.representante = ""
                    this.ips.nivel_de_atencion = ""

                    axios.get('http://127.0.0.1:8000/ips/')
                    .then( response => {
                        this.ips_data = response.data
                        console.log(this.ips_data)
                    })
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en la actualizacion del registro.");  
                });
        },
    },

    created () {
        axios.get('http://127.0.0.1:8000/ips/')
            .then( response => {
                this.ips_data = response.data
                console.log(this.ips_data)
            })
    },
    
}
</script>





<style>
    .table-responsive{
        background: #fac6b9;
    }

    .signUp_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container_signUp_user {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 70%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .signUp_user h2{
        color: #283747;
    }
    .signUp_user form{
        width: 70%;
        
    }
    .signUp_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #283747;
    }
    .signUp_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }
    .signUp_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }
</style>