import { Component, OnInit, Input} from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-edit-add-task',
  templateUrl: './edit-add-task.component.html',
  styleUrls: ['./edit-add-task.component.css']
})
export class EditAddTaskComponent implements OnInit {

  constructor(private service:SharedService) { }
  @Input() task:any;
  TaskId:string;
  TaskName:string;
  TaskCompletion:Boolean;


  ngOnInit(): void {
    this.TaskId=this.task.TaskID;
    this.TaskName=this.task.TaskName;
  }
  addTask(){
    var request = {
      TaskName:this.task.TaskName,
      TaskCompletion:false
    };
    console.log(this.task.TaskName);
    this.service.addTasks(request).subscribe(res=>{
      alert(res.toString());
    });
  }

  updateTask(){
    var request = {
      TaskID:this.task.TaskID,
      TaskName:this.task.TaskName,
      TaskCompletion:false
    };
    this.service.updateTasks(request).subscribe(res=>{
      alert(res.toString());
    });
  }
  

}
