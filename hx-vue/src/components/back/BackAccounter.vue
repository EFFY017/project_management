<template>
  <VmTable title="管理员信息管理"
           type="edit"
           :columns="dataColumns"
           :data="dataTable"
           v-on:add-ok="add"
           v-on:edit-ok="edit"
           v-on:delete-ok="deletefn"
           class="vm-margin">
  </VmTable>
</template>

<script>
import VmTable from '../back/vm-table'
export default {
  name: 'BackAccounter',
  components: {
    VmTable
  },
  methods: {
    add: function (data) {
      this.dataTable.unshift(data)
    },
    edit: function (data) {
      this.dataTable.forEach(function (elem) {
        if (elem.id === data.id) {
          for (let i in data) {
            elem[i] = data[i]
          }
        }
      })
    },
    deletefn: function (data) {
      for (let i = 0; i < this.dataTable.length; i++) {
        for (let j = 0; j < data.length; j++) {
          if (this.dataTable[i].id === data[j].id) {
            this.dataTable.splice(i, 1)
          }
        }
      }
    }
  },
  data () {
    return {
      dataColumns: [
        {
          id: '20156541',
          title: '用户名',
          key: 'username'
        },
        {
          id: '20156542',
          title: '密码',
          key: 'password'
        }
      ],
      dataTable: [
        {
          username: 'admin',
          password: '123456'
        },
        {
          username: '1',
          password: '123456'
        },
        {
          username: '2',
          password: '123456'
        },
        {
          username: '3',
          password: '123456'
        },
        {
          username: '4',
          password: '123456'
        },
        {
          username: '5',
          password: '123456'
        }
      ]
    }
  }
}
</script>
