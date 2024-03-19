#include<iostream>
#include<queue>
#include<iomanip>
#include<map>
#include<string>
#include<limits>
#include<vector>
using namespace std;

//PROCESS CLASS
class process{
    //process number, burst time, arrival time, completion time, waiting time, burst time left, turn around time
    int pno,bt,ct,at,wt,btLeft,tat; 
    static int pcounter;
    public:
    process(){
        while(true){
            cout<<"Enter process No."<<++pcounter<<"'s details below\n";
            pno=pcounter;
            cout<<"Arrival Time: ";cin>>at;
            if(at < 0){
                cout<<"\nInvalid Arrival Time. Please enter a non-negative number.\n";
                --pcounter; 
                continue;
            }
            cout<<"Burst time: ";cin>>bt;
            if(bt <= 0) {
                cout<<"\nInvalid Burst Time. Please enter a positive number.\n"; 
                --pcounter; 
                continue;
            }
            cout<<endl;
            btLeft=bt;
            break;
        }
    }
    friend void ganttChart();
    friend void processTable();
    friend process* shortestJob();
    friend void shortestJobFirst(process arr[],int n);
};

int process::pcounter;

//DATA STRUCTURES
//2 queues. 1 for holding all processes and another for the dynamic readyQueue
deque<process*>processQ;
//readyQ can have atmost 1 process at all the times
deque<process*>readyQ;
//1 ordered map for the gantt chart
map<int,int>gc;
//1 vector to store the waiting processes
vector<process*>waitingQ;

//CHARTS AND TABLES
void processTable(){
    cout<<endl<<setw(51)<<right<<"PROCESS TABLE\n";
    cout<<"| P No. | Arrival Time | Burst Time | Completion Time | Turn Around Time | Waiting Time |\n";
    for(auto i: processQ){
        //cout<<string(82,'_');
        cout<<"|  "<<setw(3)<<right<<i->pno<<"  |      "<<setw(3)<<right<<i->at<<"     |     "<<setw(3)<<right<<i->bt<<"    |       "<<setw(3)<<right<<i->ct<<"       |       "<<setw(3)<<right<<i->tat<<"        |      "<<setw(3)<<right<<i->wt<<"     |"<<endl;
    }
}

//GANTT CHART
void ganttChart(){
    cout<<"\nGANTT CHART\n";
    //cout<<"| <time in ms> P No. |\n";
    cout<<"|";
    //first element till last
    for (auto it = gc.begin(); it != gc.end(); ++it) cout<<" <"<<it->first<<"> P"<<it->second<<" |";
}

//returns a process which has the smallest burst time in the waitingQ
process* shortestJob(){
    process *smallestBT=NULL;
    int min=INT_MAX,processIndex=0;
    //find process with smallest burst time
    for(int i=0;i<waitingQ.size();i++){
        if(waitingQ[i]->bt<min){
            smallestBT=waitingQ[i];
            min=waitingQ[i]->bt;
            processIndex=i;
        }
    }
    waitingQ.erase(waitingQ.begin()+processIndex);
    //DEBUG:
    //if(waitingQ.empty()){cout<<"\nWaiting Queue empty!!\n";}
    return smallestBT;
}

//SHORTEST JOB FIRST FUNCTION
void shortestJobFirst(process arr[],int n){
    int counter=0; //optimisation for checking if anything has arrived at that time
    bool complete = false; //to end the loop when all processes are finished

    //push all the processes into processQ
    for(int i=0;i<n;i++) processQ.push_back(&arr[i]);

    //DEBUG: processQueue check
    // cout<<"DEBUG: Process Queue's Burst Times\n";
    // for(auto i: processQ) cout<<i->pno<<") "<<i->btLeft<<endl; 

    //run a for loop until all process's btleft hits 0
    for(int time=0;!complete;time++){
        //DEBUG:
        //cout<<"Inside For Loop\n";

        //checking if any process has arrived now (optimised)
        if(counter<n) for(auto i: processQ) if(i->at==time){
            waitingQ.push_back(i);
            counter++;}

        //decrease burstTime of front process every ms
        //3 cases--> 
        //1) if both readyQ and waitingQ are empty then idle (continue) but also check if all processes are done or not.
        //2) only readyQ is empty and waitingQ is not empty so, take the smallest bt process from waitingQ and put it into readyQ. 
        //3) readyQ is not empty, so decrease front process of readyQ's btleft.
        //case 1
        if(readyQ.empty()&& waitingQ.empty()){
            int count=0;
            //checking if all process's btleft hits 0 or not
            for(int i=0, count=0;i<n;i++){
                //DEBUG:
                //cout<<endl<<processQ[i]->btLeft<<endl;
                if(processQ[i]->btLeft!=0) break;
                else count++;
                if(count==n) complete=true;
            }
            //if there are still processes which havent arrived then idle by continuing
            continue;
        }
        //case 2
        else if(readyQ.empty() && !waitingQ.empty()){
            process* frontProcess=shortestJob();
            //DEBUG:
            // cout<<"from waitingQ to readyQ\n"<<frontProcess->btLeft;
            if(frontProcess->at==time);
            //reduce btLeft
            else frontProcess->btLeft--;
            readyQ.push_front(frontProcess);
        }
        //case 3
        else if(!readyQ.empty()){
            process* frontProcess = readyQ.front();
            if(frontProcess->at==time);
            //reduce btLeft
            else frontProcess->btLeft--;
            //DEBUG:
            //cout<<frontProcess->btLeft<<endl; 
        }
    
        //pop only if front process btLeft hits 0
        if(readyQ.front()->btLeft==0){
            //remove from ready queue to mutate
            process* frontProcess2 = readyQ.front();
            readyQ.pop_front();

            //for gantt chart. make a <time,pno> pair and feed into gc ordered map
            pair<int,int> stamp(time,frontProcess2->pno);
            gc.insert(stamp);

            //record all data
            frontProcess2->ct=time;
            frontProcess2->tat=frontProcess2->ct-frontProcess2->at;
            frontProcess2->wt=frontProcess2->tat-frontProcess2->bt;
            //DEBUG:
            //if(readyQ.empty()){cout<<"\nREADT QUEUEU EMPTY\n";}

            //if waitingQ is not empty then take the next process with smallest bt and put into readyQ
            if(!waitingQ.empty()) {
                process* newFrontProcess=shortestJob();
                readyQ.push_front(newFrontProcess);
            }
        }

    }
    //DEBUG: check everything
    // cout<<"Arrival time\n";
    // for(auto i: processQ) cout<<setw(2)<<i->at<<" ";
    // cout<<"\nBurst time\n";
    // for(auto i: processQ) cout<<setw(2)<<i->bt<<" ";
    // cout<<"\nCompletion time\n";
    // for(auto i: processQ) cout<<setw(2)<<i->ct<<" ";
    // cout<<"\nTurn around time\n";
    // for(auto i: processQ) cout<<setw(2)<<i->tat<<" ";
    // cout<<"\nWaiting time\n";
    // for(auto i: processQ) cout<<setw(2)<<i->wt<<" ";
    // cout<<endl;

    //to display process details
    processTable();

    //to display gantt chart
    ganttChart();

    //calculate average turn around time and waiting time
    double avgtat=0,avgwt=0;
    for(auto i: processQ){
        avgtat=avgtat+i->tat;
        avgwt=avgwt+i->wt;
    }
    avgtat=avgtat/n;
    avgwt=avgwt/n;

    //display the atat and awt
    cout<<"\n\nAverage Turn Around time: "<<setprecision(4)<<avgtat<<" ms"<<endl;
    cout<<"Average Waiting Time: "<<setprecision(4)<<avgwt<<" ms\n\n";
}

void initiator(){
    while(true){
        int num;
        cout<<"\nEnter number of processes: ";
        cin>>num;
        // Check if input is valid
        if(cin.fail()){ 
            cout << "Invalid input. Please enter a valid number." << endl;
            cin.clear(); // Clear the error state
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            continue;
        }
        if(num<=0){
            cout << "Please enter a valid positive integer for the number of processes." << endl;
            continue;
        }
        cout << endl;
        process arr[num];
        shortestJobFirst(arr,num);
        break;
    }
}

int main(){
    initiator();
    return 0;
}