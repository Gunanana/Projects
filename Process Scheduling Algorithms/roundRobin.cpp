#include<iostream>
#include<queue>
#include<iomanip>
using namespace std;

//arrival time considered 0
class process{
    int pno,bt,at=0,ct,wt,btLeft,tat; //burst time, arrival time, completion time, waiting time, burst time left, turn around time
    static int pcounter;
    public:
    process(){
        cout<<"Enter process No."<<++pcounter<<"'s details below\n";
        pno=pcounter;
        cout<<"Enter burst time: ";cin>>bt;
        btLeft=bt;
        //cout<<"Enter arrivalTime: ";cin>>at;
    }
    friend int totalBurstTime(process arr[],int);
    friend void roundRobin(process arr[],int q,int n);
};

int process::pcounter;

//return totalBurstTime so that the roundrobin loop can run till all processes are completed
int totalBurstTime(process arr[],int n){
    int totbt=0;
    for(int i=0;i<n;i++) totbt=totbt+arr[i].bt;
    return totbt;
}

void roundRobin(process arr[],int quantum,int n){
    int q=1;
    deque<process*>readyQ;

    //push all the processes into a queue
    for(int i=0;i<n;i++) readyQ.push_back(&arr[i]);
    //readyQueue check
    //for(int i=0;i<n;i++) cout<<(*readyQ[i]).btLeft<<endl; 

    int totbt=totalBurstTime(arr,n); 
    //totbt check
    //cout<<"Total burst time is: "<<totbt<<" ms."<<endl; 

    //run a for loop for totbt ms
    for(int i=1;i<=totbt;i++){
        q++;
        readyQ.front()->btLeft--; //decrease burstTime every ms
        //pop only if q ms has passed or process btLeft hits 0
        if((q==quantum|| readyQ.front()->btLeft==0)){
            q=0;
            process* frontProcess = readyQ.front();
            readyQ.pop_front();
            if(frontProcess->btLeft>0) readyQ.push_back(frontProcess);//if btLeft>0, push it back
            //else record the completionTime, calculate the turnaround and waiting time. dont push it back
            else if(frontProcess->btLeft==0){
                frontProcess->ct=i;
                frontProcess->tat=frontProcess->ct-frontProcess->at;
                frontProcess->wt=frontProcess->tat-frontProcess->bt;
            }
        }
    }

    //ct check
    // cout<<"Their completion time\n";
    // for(int i=0;i<n;i++){
    //     cout<<arr[i].ct<<endl;
    // }

    //find average turn around time and waiting time
    float avgtat=0,avgwt=0;
    for(int i=0;i<n;i++){
        avgtat=avgtat+arr[i].tat;
        avgwt=avgwt+arr[i].wt;
    }
    avgtat=avgtat/n;
    avgwt=avgwt/n;

    cout<<"\nAverage Turn Around time: "<<setprecision(4)<<avgtat<<" ms"<<endl;
    cout<<"Average Waiting Time: "<<setprecision(4)<<avgwt<<" ms"<<endl;
}

int main(){
    int num,quantum;
    cout<<"Enter number of processes: ";cin>>num;
    cout<<"Enter quantum time: ";cin>>quantum;
    process arr[num];
    roundRobin(arr,quantum,num);
}

